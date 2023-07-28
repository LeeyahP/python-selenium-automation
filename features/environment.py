from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #context.driver = webdriver.Chrome(
        #chrome_options=options,
        #service=service
    #)

### BROWSERSTACK ###
    desired_cap = {
        'browser': 'Safari',
        'os_version': '13',
        'os': 'OSX',
        'name': test_name
    }
    bs_user ="leeyahpmoore_nHjoBf"
    bs_key = "u75gCHgsRTJAvK5kpyTF"
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    #context.driver = webdriver.Firefox(executable_path=r'C:\Users\leeya\automation\CureSkin-Automation-Internship\geckodriver.exe')
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()