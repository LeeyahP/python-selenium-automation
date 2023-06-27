from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
PRODUCT_NAME = (By.ID, 'title')
CART_PAGE = (By.ID, 'nav-cart-count-container')
ITEM_NAME = (By.CSS_SELECTOR, 'span.a-truncate-cut')

@when('Open cart page')
def open_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(CART_PAGE))
    context.driver.find_element(CART_PAGE).click()


@then('Validate cart has correct item')
def correct_item(context):
    context.driver.wait.until(EC.element_to_be_clickable(ITEM_NAME))
    actual_name = context.driver.find_element(ITEM_NAME).text
    assert context.product_name [:30] in actual_name, f'Expected {context.product_name} but got {actual_name}'