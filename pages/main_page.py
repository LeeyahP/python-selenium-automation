from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By


class MainPage(Page):
    X_BTN = (By.CSS_SELECTOR, '.popup-close')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')
        sleep(7)

    def close_coupon_box(self):
        self.click(*self.X_BTN)
        sleep(7)
