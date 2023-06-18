from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
PRODUCT_NAME = (By.ID, 'title')
@when('Open cart page')
def open_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@then('Validate cart has correct item')
def correct_item(context):
    actual_name = context.driver.find_element(By.CSS_SELECTOR, 'span.a-truncate-cut').text
    assert context.product_name [:30] in actual_name, f'Expected {context.product_name} but got {actual_name}'