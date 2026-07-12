# Bilgisayar Mimarisi: RISC-V Tabanlı Yaklaşım

**Oğuz Ergin** — TOBB ETÜ

**Sürüm 0.4.7** — 6 bölüm + 4 ek yayında (528 sayfa)

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18903609.svg)](https://doi.org/10.5281/zenodo.18903609)

---

## PDF İndir

Kitabın güncel PDF sürümünü doğrudan indirmek için:

📥 **[Kitabı İndir (PDF)](https://github.com/prof-oguzergin/bilgisayar-mimarisi/releases/latest/download/bilgisayar-mimarisi.pdf)**

## Video Dersler

Kitaba eşlik eden video ders serisi YouTube'da yayınlanmaktadır:

🎬 **[Bilgisayar Mimarisi — Video Dersler](https://www.youtube.com/playlist?list=PLvNq8wrSYGAU6CF4UleG6HbXa9paQDsLK)**

## Hakkında

Bu kitap, RISC-V buyruk kümesi mimarisi temelinde yazılmış Türkçe bir bilgisayar mimarisi ders kitabıdır. Lisans düzeyinde bilgisayar mühendisliği ve elektrik-elektronik mühendisliği öğrencilerine yönelik olarak hazırlanmıştır.

**Sürekli güncellenen açık erişimli bir ders kitabıdır.** Hata bildirimleri memnuniyetle karşılanır.

## İçindekiler

| Bölüm | Konu | Durum |
|-------|------|-------|
| 1 | Giriş | ✅ Yayında |
| 2 | Başarım | ✅ Yayında |
| 3 | Buyruk Kümesi Mimarisi | ✅ Yayında |
| 4 | RISC-V ile Programlama | ✅ Yayında |
| 5 | Aritmetik İşlemler | ✅ Yayında |
| 6 | İşlemci Tasarımı | ✅ Yayında |
| 7 | Boru Hattı | 🔧 Hazırlanıyor |
| 8 | Bellek Hiyerarşisi | 🔧 Hazırlanıyor |
| 9 | Giriş/Çıkış | 🔧 Hazırlanıyor |
| 10 | Çok Çekirdekli İşlemciler | 🔧 Hazırlanıyor |
| 11 | GPU ve Hızlandırıcılar | 🔧 Hazırlanıyor |
| 12 | Güncel Mimariler | 🔧 Hazırlanıyor |
| Ek A | Sayı Sistemleri ve Kodlama | ✅ Yayında |
| Ek B | Sayısal Tasarım Temelleri | ✅ Yayında |
| Ek C | RISC-V Referans Kartı | ✅ Yayında |
| Ek D | Uygulamalı Çalışma Rehberi | ✅ Yayında |

## Derleme

Kitabı derlemek için LuaLaTeX gereklidir:

```bash
# Tüm kitabı derle
lualatex ana-kitap.tex
biber ana-kitap
lualatex ana-kitap.tex
lualatex ana-kitap.tex

# Yalnızca belirli bir bölümü derle
# ana-kitap.tex içinde \includeonly satırını düzenleyin
```

### Gereksinimler

- [TeX Live](https://www.tug.org/texlive/) 2024+ veya [MiKTeX](https://miktex.org/) 24.1+
- LuaLaTeX
- Biber (kaynakça yönetimi)

## Atıf

Bu kitabı akademik çalışmalarınızda kullanıyorsanız lütfen aşağıdaki şekilde atıf yapınız:

```bibtex
@book{ergin2026bilgisayar,
  author    = {Ergin, Oğuz},
  title     = {Bilgisayar Mimarisi: RISC-V Tabanlı Yaklaşım},
  year      = {2026},
  isbn      = {978-625-00-6081-0},
  publisher = {Açık Erişim},
  url       = {https://github.com/prof-oguzergin/bilgisayar-mimarisi},
  doi       = {10.5281/zenodo.18903609},
  license   = {CC BY-NC-ND 4.0},
  note      = {Sürekli güncellenen açık erişimli ders kitabı}
}
```

## Lisans

Bu eser [Creative Commons Atıf-GayriTicari-Türetilemez 4.0 Uluslararası](https://creativecommons.org/licenses/by-nc-nd/4.0/) lisansı ile lisanslanmıştır.

Özgürce paylaşabilir ve dağıtabilirsiniz — uygun atıf yapmanız, ticari amaçla kullanmamanız ve değişiklik yapmamanız koşuluyla. Ticari kullanım veya uyarlama izni için yazarla iletişime geçiniz.
