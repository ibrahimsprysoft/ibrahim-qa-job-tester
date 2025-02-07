from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CareersPage(BasePage):
    # Locators
    INSIDER_LOCATIONS_WIDGET = (By.CSS_SELECTOR, "[data-widget_type='wp-widget-insider-locations.default']")
    INSIDER_CAREER_WIDGET = (By.CSS_SELECTOR, "[data-widget_type='wp-widget-insider-career.default']")
    LIFE_AT_INSIDER_SECTION = (By.XPATH, "//h2[text()='Life at Insider']//ancestor::section")
    
    QA_JOBS_URL = "https://useinsider.com/careers/quality-assurance/"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/careers"

    def verify_careers_page_sections(self):
        return all([
            self.is_element_visible(*self.INSIDER_LOCATIONS_WIDGET),
            self.is_element_visible(*self.INSIDER_CAREER_WIDGET),
            self.is_element_visible(*self.LIFE_AT_INSIDER_SECTION),
            self.url in self.driver.current_url,
        ])


    def go_to_qa_jobs(self):
        self.driver.get(self.QA_JOBS_URL) 