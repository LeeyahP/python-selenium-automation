from selenium.webdriver.common.by import By
from behave import given, when, then
from app.application import Application

CATEGORY = (By.XPATH, '//span[text()="Shop by Category"]')


@given('Open main page')
def open_cure_skin_main(context):
    context.app.main_page.open_main_page()


@when('Click to "Shop by category" - select Body')
def shop_category_body(context):
    context.app.header.click_category_btn()


@then('Verify "Body" header is shown')
def verify_url_contains_query(context, body):
    context.app.search_results.verify_body_text(body)
