from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)
        self.main_window = None

    def wait_for_page_load(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        self.wait.until(lambda driver: driver.execute_script("return window.jQuery ? jQuery.active === 0 : true"))
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)  # Ek güvenlik için kısa bir bekleme

    def hover_element(self, by, value):
        self.wait_for_page_load()
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        self.actions.move_to_element(element).perform()
        time.sleep(1)

    def click_element(self, by, value):
        self.wait_for_page_load()
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        time.sleep(1)
        self.actions.move_to_element(element).perform()
        element.click()

    def is_element_visible(self, by, value):
        self.wait_for_page_load()
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        return element.is_displayed()

    def get_element_text(self, by, value):
        self.wait_for_page_load()
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        return element.text

    def store_main_window(self):
        """Ana pencere handle'ını saklar"""
        self.main_window = self.driver.current_window_handle

    def switch_to_new_window(self):
        """Yeni açılan pencereye geçiş yapar"""
        self.wait.until(lambda d: len(d.window_handles) > 1)
        for window in self.driver.window_handles:
            if window != self.main_window:
                self.driver.switch_to.window(window)
                break
        self.wait_for_page_load()

    def switch_to_main_window(self):
        """Ana pencereye geri döner"""
        if self.main_window:
            self.driver.switch_to.window(self.main_window)
            self.wait_for_page_load()

    def close_current_window(self):
        """Mevcut pencereyi kapatır ve ana pencereye döner"""
        self.driver.close()
        self.switch_to_main_window() 