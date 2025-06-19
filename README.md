# CAMO_FOR_CV

## Proje Hakkında
Bu proje, kargo paketleme sürecini otomatikleştirmek için geliştirilmiş kamera destekli bir takip sistemidir. Paket üzerindeki etiketten ismi okuyarak (OCR teknolojisi) paketleme videosu ile müşteri bilgilerini aynı klasör içinde saklar. Ayrıca bu bilgileri Microsoft SQL Server (TSQL) veritabanına kaydeder.

## Özellikler
- Gerçek zamanlı kamera görüntüsü ile paket etiketi üzerindeki isim bilgisi okuma
- Paketleme işlemi videosu kaydı ve kaydın ilgili kişi bilgisi dosyası ile eşleştirilmesi
- Kişisel bilgilerin (Ad, Soyad, Adres vb.) dosya olarak kaydedilmesi
- TSQL kullanan veritabanı ile paket ve kullanıcı bilgileri takibi
- Basit ama etkili veritabanı yönetimi için C# tabanlı veri kaydetme modülü
- Hata yakalama ve kullanıcı bilgilendirme

## Gereksinimler
- Python 3.11 veya üzeri
- Microsoft Visual C++ Derleyici (C++ modülünün derlenmesi için)
- Microsoft SQL Server (T-SQL destekli veritabanı)
- .NET Framework veya .NET Core (C# modülünü çalıştırmak için)
- Python pip paketleri: opencv-python, pytesseract
- Tesseract-OCR kurulu ve sistem PATH’inde olması gerekmektedir

## Kurulum ve Çalıştırma

### 1. Python Ortamını Hazırlama
```bash
pip install opencv-python pytesseract
```
# Windows için: 
- https://github.com/tesseract-ocr/tesseract/releases adresinden uygun sürüm indirilmeli
- Kurulum sonrası PATH değişkenine tesseract yolu eklenmeli

### 2. DLL Derlenmesi (C++ Video Yakalama Modülü)
- Proje içinde bulunan C++ kaynak kodunu uygun derleyici (MinGW, Visual Studio) ile derleyin:
```bash
cmake .
cmake --build .
```

- "CAMO_CM_CPP.dll" dosyasını Python projesinin kök dizinine yerleştirin.

### 3. Microsoft SQL Server Kurulumu
- SQL Server servisini kurup çalıştırın
- Veritabanı ve tabloları oluşturun (şema örnekleri sağlayabilirsiniz)
- C# uygulamasındaki bağlantı dizisini (connection string) kendi ortamınıza göre düzenleyin

### 4. Uygulamayı Çalıştırma
- Python scriptini başlatın:
```bash
python CAMO_CM_Python#2.py
```
- Kamera paketi algılar ve belirtilen bilgilere göre kayıt yapar.

### Proje Dosya Yapısı
```bash
/DATASERVICE           # Paketleme videoları ve bilgi dosyalarının kaydedildiği klasör (otomatik oluşturulur)
/MultipleFiles         # Kaynak kod dosyaları
  CAMO_CM_CPP#2.cpp       # C++ video yakalama kodu
  CAMO_CM_CSHARP#2.cs     # SQL Server veri kaydetme uygulaması
  CAMO_CM_Python#2.py     # Ana Python uygulaması (kamera, OCR, video kaydı)
  CMakeLists.txt          # C++ derleme ayarları
/publicindex.html          # Kişi bilgileri arama için basit web arayüzü (opsiyonel)
/CAMO_CM_JavaScript#2.js   # Basit backend Node.js uygulaması (opsiyonel)
README.md                  # Proje dökümantasyonu
.gitignore                 # Git ignore ayarları
LICENSE                   # Proje lisansı
```

### Kullanım
- Paket odaya girildiğinde uygulama kamera açılır ve canlı yayına başlar
- Paket üzerindeki etiket üzerindeki isim OCR ile okunur
- Paketleme süreci video olarak kaydedilir
- Okunan bilgiler (isim, soyisim, adres vb.) metin dosyası halinde kaydedilir
- Video ve metin dosyaları aynı klasörde tutulur
- Veritabanına paket ve müşteri bilgileri kaydedilir
- Opsiyonel olarak web arayüzü üzerinden kişi bilgileri aranabilir

### Geliştirme ve Katkı
Proje açık kaynak olarak geliştirilmekte olup, katkılarınızı memnuniyetle karşılarız.
Lütfen hata bildirmek veya özellik talep etmek için issue açınız. Pull request göndermekten çekinmeyiniz.

### İletişim
- Herhangi bir soru veya destek talebi için aşağıdaki iletişim adresleri kullanılabilir:

# E-posta: [taha.sezer@istun.edu.tr]


