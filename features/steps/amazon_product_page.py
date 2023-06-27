from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
PRODUCT_NAME = (By.ID, 'title')
PRODUCT_PRICE = (By.XPATH, "//span[@class='a-price-whole']")
ADD_CART_BTN = (By.CSS_SELECTOR, '#add-to-cart-button')
SIZE = (By.CSS_SELECTOR, '#variation_size_name')
CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')
CLICK_PRODUCT = (By.CSS_SELECTOR, '.a-price-whole')
COLOR_OPTIONS = (By.CSS_SELECTOR,'.imgSwatch' )
CURRENT_COLOR = (By.CSS_SELECTOR, '.selection')

@when('Click on product')
def click_product(context):
    #context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_PRICE))
    context.driver.find_element(PRODUCT_PRICE).click()


@when('Add product to cart')
def add_product(context):
    #context.driver.wait.until(EC.element_to_be_clickable(ADD_CART_BTN))
    context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()


@when('Select size')
def select_size(context):
    #context.driver.wait.until(EC.element_to_be_clickable(SIZE))
    context.driver.find_element(SIZE).click()


@then('Verify cart has {expected_amount} item')
def verify_cart(context, expected_amount):
    #context.driver.wait.until(EC.element_to_be_clickable(CART_COUNT))
    count = context.driver.find_element(CART_COUNT).text
    assert count == expected_amount


@when('Store product name')
def name_of_product(context):
    #context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_NAME))
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product : {context.product_name}')


@when('Click On Color Product')
def color_option_product_page(context):
    context.driver.find_element(*CLICK_PRODUCT).click()

@when('Select Colors')
def color_option_product_page(context):
    expected_colors =['Black','Camel','Coral Pink','Ivory','Lilac', 'Navy', 'Turquoise Blue']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors
