import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--start-maximized')
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_insider_qa_positions(driver):
    # 1. Ana sayfayı aç ve kontrol et
    home_page = HomePage(driver)
    home_page.navigate_to()
    assert home_page.verify_home_page(), "Ana sayfa açılamadı"

    # 2. Careers sayfasına git ve bölümleri kontrol et
    home_page.click_company_menu()
    home_page.click_careers()
    careers_page = CareersPage(driver)
    assert careers_page.verify_careers_page_sections(), "Careers sayfası bölümleri görüntülenemiyor"

    # 3. QA pozisyonlarını filtrele
    careers_page.go_to_qa_jobs()
    qa_jobs_page = QAJobsPage(driver)
    qa_jobs_page.click_see_all_jobs()
    qa_jobs_page.filter_by_location("Istanbul, Turkiye")
    qa_jobs_page.filter_by_department("Quality Assurance")

    # 4. İş ilanlarını kontrol et
    assert qa_jobs_page.verify_job_listings(), "İş ilanları kriterlere uygun değil"

    # 5. View Role butonuna tıkla ve Lever formunu kontrol et
    qa_jobs_page.click_view_role()
    assert "lever.co" in driver.current_url, "Lever başvuru formuna yönlendirme başarısız" 