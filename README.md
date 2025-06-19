# CAMO_FOR_CV#2

## Proje Hakkında
- Bu proje, kargo paketleme sürecini otomatikleştirmek için geliştirilmiş kamera destekli bir takip sistemidir. 
- Paket üzerindeki etiketten ismi okuyarak (OCR teknolojisi) paketleme videosu ile müşteri bilgilerini aynı klasör içinde saklar. 
- Ayrıca bu bilgileri Microsoft SQL Server (TSQL) veritabanına kaydeder.

## Özellikler
- Gerçek zamanlı kamera görüntüsü ile paket etiketi üzerindeki isim bilgisi okuma.
- Paketleme işlemi videosu kaydı ve kaydın ilgili kişi bilgisi dosyası ile eşleştirilmesi.
- Kişisel bilgilerin (Ad, Soyad, Adres vb.) dosya olarak kaydedilmesi.
- TSQL kullanan veritabanı ile paket ve kullanıcı bilgileri takibi.
- Basit ama etkili veritabanı yönetimi için C# tabanlı veri kaydetme modülü.
- Hata yakalama ve kullanıcı bilgilendirme.

## Gereksinimler

- Python 3.11 veya üzeri
- Microsoft Visual C++ Derleyici (C++ modülünün derlenmesi için).
- Microsoft SQL Server (T-SQL destekli veritabanı).
- .NET Framework veya .NET Core (C# modülünü çalıştırmak için).
- Python pip paketleri: opencv-python, pytesseract.
- Tesseract-OCR kurulu ve sistem PATH’inde olması gerekmektedir.

## Kurulum ve Çalıştırma

 ### 1. Python Ortamını Hazırlama
``` bash
pip install opencv-python pytesseract
```
 #### Windows için:
 - https://github.com/tesseract-ocr/tesseract/releases adresinden uygun sürüm indirilmeli.
 - Kurulum sonrası PATH değişkenine tesseract yolu eklenmeli.

 ### 2. DLL Derlenmesi (C++ Video Yakalama Modülü)
- Proje içinde bulunan C++ kaynak kodunu uygun derleyici (MinGW, Visual Studio) ile derleyin:
``` bash
cd CAMO_FOR_CV_2\CAMO_FOR_CV#2CPP
mkdir build && cd build
cmake .. && make
```
- "CAMO_CM_CPP.dll" dosyasını Python projesinin kök dizinine yerleştirin.

### 3. Microsoft SQL Server Kurulumu
- SQL Server servisini kurup çalıştırın.
- Veritabanı ve tabloları oluşturun (şema örnekleri sağlanacaktır).
- C# uygulamasındaki bağlantı dizisini (connection string) kendi ortamınıza göre düzenleyin.

### 4. Uygulamayı Çalıştırma
- Python scriptini başlatın:
``` bash
cd CAMO_FOR_CV_2\CAMO_FOR_CV_2#PY&API
python CAMO_FOR_CV_2\CAMO_FOR_CV_2#PY&API\CAMO_FOR_CV_2_PY#api_gateway.py
```
- Kamera paketi algılar ve belirtilen bilgilere göre kayıt yapar.
- Web sunucusunu başlatın:
```bash
cd CAMO_FOR_CV_2\CAMO_FOR_CV_2#Front
node CAMO_FOR_CV_2\CAMO_FOR_CV_2#Front\CAMO_FOR_CV_2#server.js
```

## Proje Dosya Yapısı

``` bash
sadece örnek bir şema
cargo-tracking-system/
├── backend/
│   ├── cpp/                  # Kamera yakalama (C++)
│   │   ├── CMakeLists.txt
│   │   ├── camo_capture.cpp
│   ├── csharp/               # Veritabanı işlemleri (C#)
│   │   ├── DatabaseManager.cs
│   │   └── DatabaseManager.csproj
│   └── python/               # API & OCR (Python)
│       ├── api_gateway.py
│       ├── ocr_processor.py
│       └── requirements.txt
└── README.md                 # Proje dökümantasyonu
```
## Kullanım
- Paket odaya girildiğinde uygulama kamera açılır ve canlı yayına başlar.
- Paket üzerindeki etiket üzerindeki isim OCR ile okunur.
- Paketleme süreci video olarak kaydedilir.
- Okunan bilgiler (isim, soyisim, adres vb.) metin dosyası halinde kaydedilir.
- Video ve metin dosyaları aynı klasörde tutulur.
- Veritabanına paket ve müşteri bilgileri kaydedilir.
- Opsiyonel olarak web arayüzü üzerinden kişi bilgileri aranabilir.

## Geliştirme ve Katkı
Proje açık kaynak olarak geliştirilmekte olup, katkılarınızı memnuniyetle karşılarız.
Lütfen hata bildirmek veya özellik talep etmek için issue açınız. Pull request göndermekten çekinmeyiniz.

## İletişim
- Herhangi bir soru veya destek talebi için aşağıdaki iletişim adresleri kullanılabilir:

## E-posta: [taha.sezer@istun.edu.tr]
