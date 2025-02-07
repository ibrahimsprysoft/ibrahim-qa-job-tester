# Insider QA İş İlanları Test Otomasyonu

Bu proje, Insider kariyer sayfasındaki QA pozisyonlarını test eden bir otomasyon projesidir. Selenium WebDriver ve Python kullanılarak geliştirilmiştir.

## 🚀 Test Senaryosu

1. Ana sayfa açılır ve kontrol edilir (www.useinsider.com)
2. Careers sayfasına gidilir
   - Kariyer sayfasındaki tüm bölümlerin görüntülendiği kontrol edilir
   - Konum, ekip ve yaşam alanlarının görüntülendiği kontrol edilir
3. QA pozisyonları için filtreleme yapılır
   - Tüm QA pozisyonları görüntülenir
   - İstanbul, Türkiye lokasyonu seçilir
   - Quality Assurance departmanı seçilir
4. İş ilanları kontrol edilir
   - Pozisyon başlığında "QA", "Quality Assurance" veya "Test" içerdiği kontrol edilir
   - Departmanın "Quality Assurance" olduğu kontrol edilir
   - Lokasyonun "Istanbul, Turkey" olduğu kontrol edilir
   - "View Role" butonunun görünür ve aktif olduğu kontrol edilir
5. İlk pozisyonun detayları kontrol edilir
   - "View Role" butonuna tıklanır
   - Lever başvuru formunun açıldığı kontrol edilir

## 🛠️ Kurulum

1. Python 3.11 veya üzeri sürümü yükleyin
2. Projeyi klonlayın:
```bash
git clone https://github.com/ibrahimsprysoft/ibrahim-qa-job-tester.git
cd ibrahim-qa-job-tester
```

3. Sanal ortam oluşturun ve aktif edin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac için
# veya
venv\Scripts\activate  # Windows için
```

4. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Testleri Çalıştırma

Tüm testleri çalıştırmak için:
```bash
python -m pytest tests/test_insider_careers.py -v
```


## 📁 Proje Yapısı

```
├── pages/                  # Page Object Model sınıfları
│   ├── base_page.py       # Temel sayfa sınıfı
│   ├── home_page.py       # Ana sayfa
│   ├── careers_page.py    # Kariyer sayfası
│   └── qa_jobs_page.py    # QA pozisyonları sayfası
├── tests/                 # Test dosyaları
│   └── test_insider_careers.py
├── requirements.txt       # Proje bağımlılıkları
└── README.md
```

## 🔧 Kullanılan Teknolojiler

- Python 3.11
- Selenium WebDriver
- Pytest
- Chrome WebDriver

## 📝 Notlar

- Test çalıştırmadan önce Chrome tarayıcısının yüklü olduğundan emin olun
- İnternet bağlantınızın stabil olduğundan emin olun
- Testler sırasında tarayıcı penceresini kapatmayın
- Testler yaklaşık 1-2 dakika sürebilir
