from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
HEADER_LINKS = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq div[class*=all_style_zg-tabs-li]')



@given('Open Best Sellers Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.driver.wait.until(EC.url_contains('//www.amazon.com/gp/bestsellers/'))


@then ('Verify menu has {expected_amount} links')
def menu_elements (context, expected_amount):
    expected_amount = int(expected_amount)
    elements = context.driver.find_elements(*HEADER_LINKS)
    assert len(elements) == expected_amount, f'Expected 5 elements but got{len(elements)}'