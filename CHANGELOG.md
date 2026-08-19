# Değişiklik Günlüğü

Bu dosya, kitabın sürümler arasındaki önemli değişikliklerini takip eder.

---

## [0.4.8] — 2026-08-19

### İyileştirmeler
- **Kitap genelinde dil temizliği:** İngilizceden gelen "sav: açıklama" biçimindeki iki nokta kalıbı doğal Türkçeye çevrildi (yaklaşık 510 yerde). Cümleler bölündü ya da neden-sonuç bağlacıyla kuruldu.
- **Ek A, ikiye tümleyen anlatımı yeniden kuruldu:** artık tarifin önünde amaç (çıkarmayı toplamaya çevirmek), eksi sayının tanımı, basamak ağırlığı okuması ve yeni sayaç çemberi şekli (Şekil A.1) yer alıyor.
- Ek A'da taban çevriminde gruplamanın virgülden başladığı, tam ve kesir kısmında hangi yöne ilerlendiği açıkça belirtildi.
- Arka sayfalara **Aynı Yazardan: Bilge ve Yonga** tanıtım sayfası eklendi (çocuklar için ücretsiz bilgisayar mimarisi kitapları serisi).

### Düzeltmeler
- Yazar tanıtımında "akademisyen" yerine "öğretim üyesi".
- Bölüm 2'de bir özne-yüklem uyumsuzluğu giderildi.

---

## [0.4.7] — 2026-07-12

### İyileştirmeler
- **Bölüm 4 (RISC-V ile Programlama) görsellerle zenginleştirildi:** taban-uzaklık adresleme, döngü denetim akışı, çağrı sözleşmesinde yazmaç koruma, çok fonksiyonlu çağrı zinciri, karakter dizisi ve yapı bellek yerleşimi, kabarcık sıralama geçişi, derleme araç zinciri, MMIO adres haritası, UART yoklama akışı, matris bellek düzeni ve döngü açma için 12 yeni şekil (bölümdeki şekil sayısı 6'dan 18'e çıktı)
- Bölüm 4 dizin girdileri genişletildi; "çağrı sözleşmesi" ve "yoklama" terim kutuları eklendi

### Düzeltmeler
- Siteye Google Scholar atıf meta etiketleri eklendi (indekslenmeyi kolaylaştırmak için)
- LaTeX 2025-11-01 çekirdeğiyle derleme uyumu sağlandı (yayınlanmayan bölümlerin saplama mekanizması)

---

## [0.4.6] — 2026-07-11

### Yeni bölüm
- **Bölüm 6 — İşlemci Tasarımı** eklendi
  - Tek vuruşluk veri yolu: add, sub, ori, lw, sw, beq ve jal buyruklarıyla adım adım kuruluş
  - Denetim biriminin doğruluk tablosu ve Karno haritalarıyla gerçekleştirilmesi
  - Çok vuruşluk tasarım: ara yazmaçlar, EskiPS yazmacı ve sonlu durum makinesi (SDM)
  - Mikroprogramlama: yatay ve dikey mikrokod, donanım tabanlı denetimle karşılaştırma
  - 10 çözümlü örnek (gecikme, çevrim, BBÇ ve hızlanma hesapları) ve 26 alıştırma
  - Gerçek dünya notları (Intel 4004'ten 486'ya), yanılgılar ve tuzaklar

### Kitap geneli iyileştirmeler
- İlk 6 bölüm çok modelli değerlendirmeden geçirildi, çıkan düzeltmeler uygulandı
- Düz metinde noktalı virgül yoğunluğu azaltıldı, daha doğal Türkçe akış sağlandı
- Şekil listesine kısa başlıklar eklendi (ikinci satıra taşan başlıklar giderildi)
- Terminoloji birleştirme (elde, geçirme, üretme; argüman) ve tablo em-dash temizliği
- Bölüm 6 kaynak dosyası düz UTF-8 Türkçe karakterlere dönüştürüldü

### Düzeltmeler
- Bölüm 1: "silikon" yerine tutarlı biçimde "silisyum"
- Bölüm 4: Örnek 4.8 gerçek bir yaprak fonksiyona çevrildi, Örnek 4.6 çapraz başvurusu düzeltildi
- Bölüm 5: mükerrer sözcük düzeltildi
- Ek B: gizli karakter ve şekil/tablo başvuru uyumsuzlukları giderildi

---

## [0.4.5] — 2026-05-10

### Yeni bölüm
- **Ek B — Sayısal Tasarım Temelleri** eklendi
  - Mantık kapıları (VE, VEYA, DEĞİL, NAND, NOR, XOR, XNOR) ve evrensel kapılar
  - Boole cebri, De Morgan kuramları, mini/maksi terim gösterimleri
  - Karno haritasıyla sadeleştirme (2/3/4 değişken, önemsenmeyen durumlar)
  - Birleşik yapı taşları: kod çözücü/kodlayıcı, çoklayıcı/tekleyici, toplayıcılar
    (yarım, tam, dalgalı elde, önceden elde üreten)
  - Flip-flop türleri: RS, D, T, JK; saat tetiklemesi
  - Yazmaçlar (koşut yüklemeli, kaydırmalı) ve sayaçlar (eşzamanlı/eşzamansız)
  - Mealy ve Moore durum makineleri
  - 17 çözümlü örnek (içecek otomatı, yarışma sistemi vb.)
  - Yanılgılar ve Tuzaklar bölümü (4 yanılgı + 4 tuzak)

### Ek A iyileştirmeleri
- Yanılgılar ve Tuzaklar bölümü eklendi (4 yanılgı + 4 tuzak)

### Kitap geneli iyileştirmeler
- Bölüm 2 Özet'i paragraf stiline çevrildi (B1/B3/B4/B5 ile uyumlu)
- Tüm bölümlerde em-dash (`---`) düzyazıdan temizlendi
- Terminoloji: yasak ifadeler temizlendi
  ("yani", "yazmaç dosyası", "don't care", "timing report/slack/glitch")
- İngilizce terimler için tutarlı yaklaşım: Türkçe öne, İngilizce parantezde

---

## [0.4.0] — 2026-04-04

### Yeni bölüm
- **Bölüm 5 — Aritmetik İşlemler** eklendi
  - Toplama, çıkarma ve taşma denetimi
  - Dalga eldeli ve önceden elde üreten toplayıcılar
  - Mantık işlemleri ve 32 bitlik AMB tasarımı
  - Kaydır-topla çarpma (3 yol), Booth algoritması, Wallace ağacı
  - Geri yüklemeli, geri yüklemesiz ve SRT bölme
  - IEEE 754 kayan nokta gösterimi, özel değerler (sıfır, sonsuz, NaN)
  - Koruma, yuvarlama ve yapışkan bitleri
  - Kayan nokta toplama, çarpma ve bölme (adım adım, örneklerle)
  - RISC-V kayan nokta buyrukları (F/D uzantıları, x86/ARM karşılaştırması)
  - Yapay zeka kayan nokta biçimleri: BF16, TF32, FP8 (bit düzeni şekilleri)
  - Karma duyarlık eğitimi (motivasyon, akış şeması)
  - Model bellek gereksinimleri çubuk grafiği (LLaMA, GPT-3)
  - Ağırlık dağılımı grafiği (ResNet-50, BERT, GPT-2)
  - Intel FDIV hatası ve Patriot füzesi kazası bilgi notları
  - Newton-Raphson/Goldschmidt karşılaştırma tablosu
  - 20 çözümlü örnek, 15+ alıştırma

### Kitap geneli iyileştirmeler
- Yanılgı (koyu kırmızı) ve Tuzak (koyu turuncu) başlıkları renklendirildi (tüm bölümler)
- "ÖZEL VEYA" → "Dışlayan VEYA" tutarlılığı (tüm dosyalar)
- "pozitif/negatif" → "artı/eksi" (Bölüm 5)
- lstlisting Türkçe karakter desteği (texcl=true global)
- Bölüm 4 öğrenme hedefleri biçim düzeltmesi (Bölüm 1-3 ile tutarlı)
- Bölüm 5 öğrenme hedefleri kutusu eklendi
- "Tensor Core" → "Tensör Çekirdeği"
- "denormalize" → "olağanlaştırılmamış"

---

## [0.3.5] — 2026-03-27

### Yeni bölüm
- **Bölüm 4 — RISC-V ile Programlama** eklendi
  - Çevirici dil programlama, veri yapıları, derleme çıktısı okuma
  - Gömülü sistem programlama, başarım ve eniyileme
  - 24 çözümlü örnek, 30 alıştırma

### Bölüm 1-3 güncellemeleri
- Kapsamlı terminoloji düzeltmeleri

---

## [0.2.0] — Yayınlanmadı

### Yeni bölüm
- **Bölüm 2 — Bilgisayar Başarımı** eklendi
  - Başarım tanımı ve gereksinim belirleme
  - Saat sıklığı, çevrim zamanı ve çevrim sayısı
  - Buyruk Başına Çevrim (BBÇ) ve yürütme zamanı formülü
  - İşlem hacmi ve gecikme kavramları
  - FLOPS, SPEC ve sınama programları
  - Amdahl Yasası ve başarım iyileştirme stratejileri
  - Güç-başarım dengesi ve yapay zeka iş yüklerinde enerji maliyeti
  - Tarihsel başarım eğilimleri (altın çağ, güç duvarı, çok çekirdekli dönem)
  - 34 alıştırma

### Bölüm 1 güncellemeleri
- 8 yeni sayısal alıştırma eklendi (1.21–1.28): yonga üretimi, güç tüketimi, Moore Yasası
- Şekil 1.4 görselleri yeniden oluşturuldu (masaüstü, dizüstü, akıllı telefon, sunucu, gömülü sistem)

### Terminoloji
Kitap genelinde Türkçe terim kullanımı güçlendirildi:

| İngilizce | Eski kullanım | Yeni kullanım |
|---|---|---|
| analysis | analiz | çözümleme |
| CPU | CPU | MİB (merkezi işlem birimi) |
| critical | kritik | can alıcı |
| factor | faktör | etken |
| index | indeks | dizin |
| message | mesaj | ileti |
| parallel | paralel | koşut |
| throughput | verim | işlem hacmi |
| web | web | örün |

Her terim ilk geçtiği yerde bir **terim notu** kutusuyla açıklanmıştır.

### Kapak
- Kapak görseli yeniden tasarlandı
- "1. Baskı" → "Sürüm 0.2.0"

---

## [0.1.0] — 2026-03-07

### İlk sürüm
- Bölüm 1 (Giriş) yayınlandı
- Kapak sayfası tasarımı (TikZ, PCB arka plan)
- Lisans: CC BY-NC-ND 4.0
- GitHub public repo oluşturuldu
- Release PDF yayınlandı
