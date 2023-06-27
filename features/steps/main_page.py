from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.wait = WebDriverWait(driver, 5)
SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RETURN_ORDERS_BTN = (By.CSS_SELECTOR, '#nav-orders')
SIGN_IN_TEXT = (By.XPATH, '//h1[@class="a-spacing-small"]')
SEARCH_BOX = (By.CSS_SELECTOR, '#twotabsearchtextbox')
CLICK_SEARCH_BTN = (By.CSS_SELECTOR, '#nav-search-submit-button')


@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    #driver.wait.until(EC.url_contains('//www.amazon.com/'))


@when('Click on Return Orders button')
def click_return_orders(context):
    #driver.wait.until(
        #EC.element_to_be_clickable(RETURN_ORDERS_BTN),
        #message='Return Orders Button Not Clickable').click

    context.driver.find_element(*RETURN_ORDERS_BTN).click()


@then('user is redirected to Sign In page')
def verify_sign_in(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(*SIGN_IN_TEXT).text
    assert expected_result == actual_result, f'Expected{expected_result} but got actual{actual_result}'


@when('Search for {item}')
def click_on_item(context, item):
    #context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BOX))
    context.driver.find_element(*SEARCH_BOX).send_keys(item)


@when('Click search button')
def search_icon(context):
    #context.driver.wait.until(EC.element_to_be_clickable(CLICK_SEARCH_BTN), message='Search Button Not Clickable')
    context.driver.find_element(*CLICK_SEARCH_BTN).click()


