from selenium import webdriver

def before_scenario(context, scenario):
    driver = webdriver.Firefox()

    context.webdriver = driver

def after_scenario(context, scenario):
    context.webdriver.close()