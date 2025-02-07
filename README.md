# Insider QA Test Otomasyon Projesi

Bu proje, Insider web sitesinin kariyer sayfasındaki QA pozisyonlarını test eden bir otomasyon projesidir.

## Gereksinimler

- Python 3.8+
- Chrome tarayıcı

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [repo-url]
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Testleri Çalıştırma

Testleri çalıştırmak için:
```bash
pytest tests/test_insider_careers.py -v
```

## Proje Yapısı

- `pages/`: Page Object Model sınıfları
  - `base_page.py`: Temel sayfa sınıfı
  - `home_page.py`: Ana sayfa
  - `careers_page.py`: Kariyer sayfası
  - `qa_jobs_page.py`: QA pozisyonları sayfası
- `tests/`: Test dosyaları
  - `test_insider_careers.py`: Test senaryoları

## Test Senaryoları

1. Ana sayfa kontrolü
2. Careers sayfası ve bölümlerinin kontrolü
3. QA pozisyonlarının filtrelenmesi
4. İş ilanlarının içerik kontrolü
5. Başvuru formuna yönlendirme kontrolü 