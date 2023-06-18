from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

search = driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
search = driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
search = driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
search = driver.find_element(By.CSS_SELECTOR, '#ap_email')
search = driver.find_element(By.CSS_SELECTOR, '#ap_password')
search = driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
search = driver.find_element(By.CSS_SELECTOR, '#continue')
search = driver.find_element(By.CSS_SELECTOR, "a[href*='_notification_condition_of_use?ie=UTF8&nodeId=508088']")
search = driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")
search = driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis[href*="/ap/signin?openid.pape.max_auth_age=0&openid.return_"]')


