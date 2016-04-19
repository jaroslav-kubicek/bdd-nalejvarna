from time import sleep
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

result_selector = '//h3[@class="r"]/a[text()="Seznam.cz"]'

@given('a search phrase www.seznam.cz')
def get_phrase(context):
    global phrase

    phrase = 'www.seznam.cz'

@when('user navigates to google.com')
def navigate(context):
    context.webdriver.get('http://www.google.com')
    sleep(2) # just to see browser in action

@when('fill in the input with phrase')
def fill_in(context):
    input = context.webdriver.find_element_by_name("q")
    input.send_keys(phrase)
    input.send_keys(Keys.RETURN)

@then('google.com will find seznam.cz')
def check_result(context):
    WebDriverWait(context.webdriver, 10).until(
            EC.presence_of_element_located((By.XPATH,result_selector))
    )