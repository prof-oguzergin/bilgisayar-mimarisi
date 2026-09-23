# -*- coding: utf-8 -*-
"""Kitap sitesindeki (docs/index.html) bolum acilir listelerini .tex
kaynaklarindan uretir. Her surumde calistirilir; elle liste tutulmaz.

Yayindaki (status-ready) her bolum icin:
  - ozet satiri : sekil, tablo, bilgi notu, cozumlu ornek, alistirma sayilari
  - Alt Bolumler: numarali \\section basliklari
  - Bilgi Notlari: \\begin{bilginot}[Baslik] basliklari
  - One Cikanlar : sayfadaki mevcut elle yazilmis vurgular (sayi satirlari haric)
  - bolum fotografi alt yazisi

Bolum basliklari, gorseller ve durum etiketleri (Yayinda/Hazirlaniyor) elle
yonetilir; betik yalnizca acilir icerigi yeniden yazar.

Kullanim:  python site-icindekiler.py
"""
import io
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

KOK = os.path.dirname(os.path.abspath(__file__))
SAYFA = os.path.join(KOK, "docs", "index.html")
B = chr(92)

DOSYA = {
    "Bölüm 1": "bolum01-giris/bolum01.tex",
    "Bölüm 2": "bolum02-basarim/bolum02.tex",
    "Bölüm 3": "bolum03-buyruk-kumesi/bolum03.tex",
    "Bölüm 4": "bolum04-programlama/bolum04-programlama.tex",
    "Bölüm 5": "bolum05-aritmetik/bolum05.tex",
    "Bölüm 6": "bolum06-islemci-tasarimi/bolum06.tex",
    "Bölüm 7": "bolum07-boru-hatti/bolum07.tex",
    "Bölüm 8": "bolum08-bellek/bolum08.tex",
    "Bölüm 9": "bolum09-giris-cikis/bolum09.tex",
    "Bölüm 10": "bolum10-cok-cekirdekli/bolum10.tex",
    "Bölüm 11": "bolum11-gpu-hizlandiricilar/bolum11.tex",
    "Bölüm 12": "bolum12-guncel-mimariler/bolum12.tex",
    "Ek A": "ekA-sayi-sistemleri/ekA.tex",
    "Ek B": "ekB-sayisal-tasarim/ekB.tex",
    "Ek C": "ekC-risc-v-referans/ekC.tex",
    "Ek D": "ekD-pratik-rehber/ekD.tex",
}

# ------------------------------------------------------------------ LaTeX
def yorumsuz(t):
    """Kacisli olmayan % isaretinden satir sonuna kadar siler."""
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", s) for s in t.split("\n"))


def dengeli(t, i, ac="{", kapa="}"):
    """t[i] == ac olmali; eslesen kapanisin sonrasini ve icerigi dondurur."""
    d = 0
    for j in range(i, len(t)):
        if t[j] == ac:
            d += 1
        elif t[j] == kapa:
            d -= 1
            if d == 0:
                return t[i + 1:j], j + 1
    raise ValueError("dengesiz parantez")


AKSAN = {
    (".", "I"): "İ", ("c", "s"): "ş", ("c", "S"): "Ş", ("c", "c"): "ç", ("c", "C"): "Ç",
    ("u", "g"): "ğ", ("u", "G"): "Ğ", ('"', "o"): "ö", ('"', "O"): "Ö", ('"', "u"): "ü",
    ('"', "U"): "Ü", ("^", "a"): "â", ("^", "i"): "î", ("^", "u"): "û",
}


def duz(x):
    """Basliktaki LaTeX'i duz metne indirger."""
    # Turkce aksan komutlari: \.{I}, {\c{s}}, \c s, \u{g}, \"{o} ...
    def aksan(m):
        return AKSAN.get((m.group(1), m.group(2)), m.group(2))
    x = re.sub(re.escape(B) + r'([.cu"^])\s*\{?([A-Za-z])\}?', aksan, x)
    x = x.replace(B + "i ", "ı").replace(B + "i{}", "ı").replace("{" + B + "i}", "ı")
    for _ in range(4):
        x = re.sub(re.escape(B) + r"(?:texttt|emph|textbf|textit|textsc|mbox|text|mathrm)\{([^{}]*)\}", r"\1", x)
    x = re.sub(re.escape(B) + r"(?:index|label)\{[^{}]*\}", "", x)
    x = x.replace("``", "“").replace("''", "”").replace("---", "–").replace("--", "–")
    x = x.replace("~", " ").replace(B + " ", " ").replace(B + "&", "&").replace(B + "%", "%")
    x = x.replace(B + "_", "_").replace(B + "#", "#").replace(B + ",", " ")
    x = re.sub(r"\$([^$]*)\$", r"\1", x)
    x = re.sub(re.escape(B) + r"[a-zA-Z]+\*?", "", x)
    x = x.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", x).strip()


def cozumle(yol):
    t = yorumsuz(io.open(yol, encoding="utf-8").read())
    bolumler = []
    for m in re.finditer(re.escape(B) + r"section(?![a-zA-Z*])", t):
        i = m.end()
        while t[i] in " \n":
            i += 1
        if t[i] == "[":
            _, i = dengeli(t, i, "[", "]")
            while t[i] in " \n":
                i += 1
        if t[i] != "{":
            continue
        baslik, _ = dengeli(t, i)
        bolumler.append(duz(baslik))
    notlar = []
    for m in re.finditer(re.escape(B) + r"begin\{bilginot\}", t):
        i = m.end()
        baslik = ""
        if i < len(t) and t[i] == "[":
            baslik, _ = dengeli(t, i, "[", "]")
        notlar.append(duz(baslik) or "Bilgi Notu")

    def sayi(ortam, tur):
        n = 0
        for m in re.finditer(re.escape(B) + r"begin\{" + ortam + r"\*?\}(.*?)" + re.escape(B)
                             + r"end\{" + ortam + r"\*?\}", t, re.S):
            if re.search(re.escape(B) + r"caption(?!\*)\s*[\[{]", m.group(1)):
                n += 1
        n += len(re.findall(re.escape(B) + r"captionof\{" + tur + r"\}", t))
        return n

    return {
        "bolumler": bolumler,
        "notlar": notlar,
        "sekil": sayi("figure", "figure"),
        "tablo": sayi("table", "table") + sayi("longtable", "longtable"),
        "ornek": len(re.findall(re.escape(B) + r"begin\{ornek\}", t)),
        "alistirma": len(re.findall(re.escape(B) + r"begin\{alistirma\}", t)),
    }


# ------------------------------------------------------------------ HTML
def esc(x):
    return x.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


SAYI_SATIRI = re.compile(r"^\d+\+?\s*(?:çözümlü örnek|alıştırma|açıklayıcı şekil|şekil)\b")


def mevcut_vurgular(parca):
    for etiket in ("Öne Çıkanlar", "Özellikler"):
        m = re.search(r'acc-col-label">' + etiket + r"</div>\s*<ul>(.*?)</ul>", parca, re.S)
        if m:
            li = [re.sub(r"<[^>]+>", "", x).strip() for x in re.findall(r"<li>(.*?)</li>", m.group(1), re.S)]
            return [x for x in li if x and not SAYI_SATIRI.match(x)]
    return []


def mevcut_foto(parca):
    m = re.search(r'acc-foto">Bölüm fotoğrafı: ([^<]+)<', parca)
    if m:
        return m.group(1).strip()
    m = re.search(r'Fotoğraf</div>\s*<ul>\s*<li>([^<]+)</li>', parca)
    return m.group(1).replace(" — ", ", ").replace("—", ",").strip() if m else ""


def on_ek(ad):
    return ad.split()[1]            # "Bölüm 5" -> "5", "Ek B" -> "B"


def icerik(ad, v, vurgular, foto, girinti):
    g = girinti
    ek = on_ek(ad)
    parca = []
    if v["sekil"]:
        parca.append("%d şekil" % v["sekil"])
    if v["tablo"]:
        parca.append("%d tablo" % v["tablo"])
    if v["notlar"]:
        parca.append("%d bilgi notu" % len(v["notlar"]))
    if v["ornek"]:
        parca.append("%d çözümlü örnek" % v["ornek"])
    if v["alistirma"]:
        parca.append("%d alıştırma" % v["alistirma"])
    s = [g + '<div class="accordion-content">',
         g + '    <p class="acc-ozet">' + " · ".join(parca) + "</p>",
         g + '    <div class="acc-detail-grid">']

    def sutun(etiket, satirlar):
        s.append(g + '        <div class="acc-col">')
        s.append(g + '            <div class="acc-col-label">' + etiket + "</div>")
        s.append(g + "            <ul>")
        for x in satirlar:
            s.append(g + "                <li>" + esc(x) + "</li>")
        s.append(g + "            </ul>")
        s.append(g + "        </div>")

    sutun("Alt Bölümler", ["%s.%d %s" % (ek, i + 1, b) for i, b in enumerate(v["bolumler"])])
    if v["notlar"]:
        sutun("Bilgi Notları", ["%s.%d %s" % (ek, i + 1, n) for i, n in enumerate(v["notlar"])])
    if vurgular:
        sutun("Öne Çıkanlar", vurgular)
    s.append(g + "    </div>")
    if foto:
        s.append(g + '    <p class="acc-foto">Bölüm fotoğrafı: ' + esc(foto) + "</p>")
    s.append(g + "</div>")
    return "\n".join(s)


def main():
    html = io.open(SAYFA, encoding="utf-8", newline="").read()
    NL = "\r\n" if "\r\n" in html else "\n"
    html = html.replace("\r\n", "\n")
    ogeler = [m.start() for m in re.finditer(r'<div class="accordion-item', html)]
    rapor = []
    # sondan basa isle ki konumlar kaymasin
    for k in range(len(ogeler) - 1, -1, -1):
        bas = ogeler[k]
        parca_sonu = ogeler[k + 1] if k + 1 < len(ogeler) else html.index("</section>", bas)
        parca = html[bas:parca_sonu]
        ad = re.search(r'acc-number">([^<]+)<', parca).group(1).strip()
        if "status-ready" not in parca.split(">", 1)[0]:
            rapor.append((ad, "hazırlanıyor, dokunulmadı"))
            continue
        yol = os.path.join(KOK, DOSYA[ad])
        if not os.path.exists(yol):
            rapor.append((ad, "KAYNAK YOK: " + DOSYA[ad]))
            continue
        v = cozumle(yol)
        i0 = parca.index('<div class="accordion-content">')
        girinti = parca[parca.rindex("\n", 0, i0) + 1:i0]
        # accordion-content blogunun sonunu dengeli div sayarak bul
        d, j = 0, i0
        for m in re.finditer(r"<div\b|</div>", parca[i0:]):
            d += 1 if m.group(0) == "<div" else -1
            if d == 0:
                j = i0 + m.end()
                break
        yeni = icerik(ad, v, mevcut_vurgular(parca), mevcut_foto(parca), girinti)
        parca = parca[:i0] + yeni.lstrip() + parca[j:]
        html = html[:bas] + parca + html[parca_sonu:]
        rapor.append((ad, "%d alt bölüm, %d not, %d şekil, %d tablo, %d örnek, %d alıştırma"
                       % (len(v["bolumler"]), len(v["notlar"]), v["sekil"], v["tablo"],
                          v["ornek"], v["alistirma"])))
    io.open(SAYFA, "w", encoding="utf-8", newline="").write(html.replace("\n", NL))
    for ad, r in reversed(rapor):
        print("%-9s %s" % (ad, r))


if __name__ == "__main__":
    main()
