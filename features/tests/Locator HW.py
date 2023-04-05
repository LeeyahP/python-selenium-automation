from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

search = driver.find_element(By.XPATH, '//i[@aria-label="Amazon"]')
search = driver.find_element(By.ID, 'continue')
search = driver.find_element(By.XPATH,'//span[@class="a-expander-prompt"]')
search = driver.find_element(By.ID, 'auth-fpp-link-bottom')
search = driver.find_element(By.ID, 'ap-other-signin-issues-link')
search = driver.find_element(By.ID, 'createAccountSubmit')
search = driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
search = driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")






#driver.find_element(By.NAME, 'btnK').click()















#search.clear()
#search.send_keys('Dress')

# wait for 4 sec
sleep(4)

# click search
#driver.find_element(By.NAME, 'btnK').click()

# verify
#assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
#print('Test Passed')

#driver.quit()