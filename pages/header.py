from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):

    CATEGORY = (By.XPATH, '//*[text()="Shop by Category"]')
    BODY_BTN = (By.CSS_SELECTOR, '[data-title="Body"]')

    def click_category_btn(self):
        self.click(*self.CATEGORY)

    def click_body_btn(self):
        self.click(*self.BODY_BTN)
