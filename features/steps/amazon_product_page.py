from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
PRODUCT_NAME = (By.ID, 'productTitle')

@when('Click on product')
def click_product(context):
    context.driver.find_element(By.XPATH, "//span[@class='a-price-whole']").click()
    sleep(3)


@when('Add product to cart')
def add_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()
    sleep(3)


@when('Select size')
def select_size(context):
    context.driver.find_element(By.CSS_SELECTOR, '#variation_size_name').click()
    sleep(3)


@then('Verify cart has {expected_amount} item')
def verify_cart(context, expected_amount):
    count = context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count').text
    assert count == expected_amount


@when('Store product name')
def name_of_product(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print((f'Current product : {context.product_name}'))

