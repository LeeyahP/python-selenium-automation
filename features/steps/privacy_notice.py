from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.wait = WebDriverWait(driver, 5)
PRIVACY_NOTICE = (By.XPATH, "//a[text()='Privacy Notice']")


@given('Open Amazon T&C page')
def open_terms_and_conditions(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
    #driver.wait.until(EC.url_contains('//www.amazon.com/gp/help/customer/'))


@when('Store original windows')
def store_original_window(context):
    context.original_window = driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_privacy(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def click_privacy(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer'))


@then('User can close new window and switch back to original')
def user_goes_back_to_original_pg(context):
    context.driver.close
    context.driver.switch_to.window(context.original_window)
