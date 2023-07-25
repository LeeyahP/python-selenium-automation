from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):


    CATEGORY_NEW = (By.XPATH, "//span[@class='label' and text()='Shop by Category']")
    BODY_BTN = (By.CSS_SELECTOR, '[data-title="Body"]')

    def click_category_btn(self):
        self.wait_for_element_click(*self.CATEGORY_NEW)

    def click_body_btn(self):
        self.wait_for_element_click(*self.BODY_BTN)

