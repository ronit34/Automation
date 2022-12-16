import time

from selenium.webdriver.common.by import By


from behave import *
@then(u'Insert details with special element')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "name").send_keys("@#$%")
    context.driver.find_element(By.ID, "description").send_keys("abcd")
    context.driver.find_element(By.ID, "childtuc").send_keys(3)
    context.driver.find_element(By.ID, "smpps").send_keys(3)
    context.driver.find_element(By.ID, "smsapi").send_keys(3)


@then(u'Check error label for special character')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='namepanel']/span").text
    print(text)
    if text == "cannot contain special charaters":
        assert True, "Showing error labels"
    else:
        assert False, "Not Showing error labels"
