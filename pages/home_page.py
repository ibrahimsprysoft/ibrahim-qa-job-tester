from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):
    # Locators
    COMPANY_MENU = (By.XPATH, "//a[contains(text(), 'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(), 'Careers') and contains(@class, 'dropdown-sub')]")
    COOKIE_ACCEPT_BUTTON = (By.ID, "wt-cli-accept-all-btn")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/"

    def navigate_to(self):
        self.driver.get(self.url)
        self.accept_cookies()
        return self

    def verify_home_page(self):
        return self.driver.current_url == self.url

    def accept_cookies(self):
        try:
            self.wait_for_page_load()
            self.click_element(*self.COOKIE_ACCEPT_BUTTON)
        except TimeoutException:
            # Cookie popup'ı görünmüyorsa veya zaten kabul edilmişse devam et
            pass

    def click_company_menu(self):
        self.click_element(*self.COMPANY_MENU)

    def click_careers(self):
        self.click_element(*self.CAREERS_LINK) 