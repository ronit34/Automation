from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Verify Sub-heading and Placeholder_Notification')
def step_impl(context):
    time.sleep(2)
    subject = context.driver.find_element(By.ID, "noitf_sub").get_attribute('placeholder')
    print(subject)
    if subject == "Enter Subject":
        assert True, f"{subject}"
    else:
        assert False, f"{subject}"

    content = context.driver.find_element(By.ID, "noitf_text").get_attribute('placeholder')
    print(content)
    if content == "Enter Content":
        assert True, f"{content}"
    else:
        assert False, f"{content}"
