from selenium.webdriver.common.by import By
from behave import given, when, then


CHOOSE_BODY = (By.CSS_SELECTOR,"nav.header__inline-menu li list-menu-item[data-title='Body'")


@given('Open main page')
def open_cure_skin_main(context):
    context.app.main_page.open_main_page()
    context.app.main_page.close_coupon_box()


@when('Click to "Shop by category" - select Body')
def shop_category_body(context):
    context.app.header.click_category_btn()
    context.app.header.click_body_btn()


@then('Verify {search_query} header is shown')
def verify_url_contains_query(context, search_query):
    context.app.search_results.verify_body_text(search_query)
