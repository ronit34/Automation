from behave import *
from selenium.webdriver.common.by import By

@then(u'click on log out button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='profiledropdown']/li[4]/a").click()
    context.driver.implicitly_wait(50)


