from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Return Orders button')
def click_return_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('user is redirected to Sign In page')
def verify_sign_in(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]').text
    assert expected_result == actual_result, f'Expected{expected_result} but got actual{actual_result}'

@when('Search for {item}')
def click_on_item(context, item):
    search = context.driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
    search.send_keys(item)
    sleep(4)


@when ('Click search button')
def search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button').click()
    sleep(4)

