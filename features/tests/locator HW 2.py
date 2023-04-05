from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
sleep(2)

search = driver.find_element(By.ID,'nav-orders').click()

sleep(2)

expected_result ="Sign in"
actual_result = driver.find_element(By.XPATH,'//h1[@class="a-spacing-small"]').text
print(actual_result)

assert expected_result==actual_result, f'Expected{ expected_result } but got actual{ actual_result }'
print('Test Passed')