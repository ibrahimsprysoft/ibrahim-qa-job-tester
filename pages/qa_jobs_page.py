from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class QAJobsPage(BasePage):
    SEE_ALL_JOBS_BUTTON = (By.XPATH, "//a[text()='See all QA jobs']")
    LOCATION_FILTER = (By.CSS_SELECTOR, "[aria-labelledby='select2-filter-by-location-container']")
    DEPARTMENT_FILTER = (By.CSS_SELECTOR, "[aria-labelledby='select2-filter-by-department-container']")
    JOBS_LIST = (By.CSS_SELECTOR, ".position-list-item")
    POSITION_TITLE = (By.CSS_SELECTOR, "p.position-title")
    DEPARTMENT_TEXT = (By.CSS_SELECTOR, "span.position-department")
    LOCATION_TEXT = (By.CSS_SELECTOR, "div.position-location")
    VIEW_ROLE_BUTTON = (By.XPATH, "//a[normalize-space()='View Role']")

    FILTER_OPTION_XPATH = "//li[contains(text(), '{option}')]"

    def __init__(self, driver):
        super().__init__(driver)

    def click_see_all_jobs(self):
        self.click_element(*self.SEE_ALL_JOBS_BUTTON)
        self.wait_for_page_load()

    def _select_filter_option(self, filter_locator, option_text):
        self.click_element(*filter_locator)
        option_locator = (By.XPATH, self.FILTER_OPTION_XPATH.format(option=option_text))
        self.click_element(*option_locator)
        self.wait_for_page_load()

    def filter_by_location(self, location):
        self._select_filter_option(self.LOCATION_FILTER, location)

    def filter_by_department(self, department):
        self._select_filter_option(self.DEPARTMENT_FILTER, department)

    def verify_job_listings(self):
        self.wait_for_page_load()
        time.sleep(1)

        jobs = self.driver.find_elements(*self.JOBS_LIST)
        if not jobs:
            print("Hiç iş ilanı bulunamadı!")
            return False

        for job in jobs:
            self.actions.move_to_element(job).perform()
            time.sleep(0.5)

            try:
                position = job.find_element(*self.POSITION_TITLE).text
                department = job.find_element(*self.DEPARTMENT_TEXT).text
                location = job.find_element(*self.LOCATION_TEXT).text
            except Exception as error:
                print(f"İlan detayları alınırken hata oluştu: {error}")
                return False

            print(f"Pozisyon: {position}\nDepartman: {department}\nLokasyon: {location}")

            criteria_met = (
                any(term in position.lower() for term in ["qa", "quality assurance", "test"]) and
                "Quality Assurance" in department and
                "Istanbul, Turkiye" in location
            )
            if not criteria_met:
                print("İlan kriterlere uymuyor!")
                return False

            try:
                view_role = job.find_element(*self.VIEW_ROLE_BUTTON)
                href = view_role.get_attribute("href")
                if view_role.is_displayed() and href:
                    print(f"View Role bulundu: {href}")
            except Exception:
                print("View Role butonu görünür değil.")
        return True

    def click_view_role(self):
        jobs = self.driver.find_elements(*self.JOBS_LIST)
        if not jobs:
            print("İlan bulunamadı!")
            return

        first_job = jobs[0]
        self.actions.move_to_element(first_job).perform()
        time.sleep(0.5)
        
        try:
            view_role = first_job.find_element(*self.VIEW_ROLE_BUTTON)
            href = view_role.get_attribute("href")
            
            if not href:
                print("View Role butonunda href bulunamadı!")
                return
            
            self.store_main_window()
            
            view_role.click()
            
            self.switch_to_new_window()
            print("Yeni sekmeye geçildi!")
            
        except Exception as error:
            print(f"View Role tıklanırken hata oluştu: {error}")
            self.switch_to_main_window()