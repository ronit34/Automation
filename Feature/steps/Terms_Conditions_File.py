from behave import *
from selenium.webdriver.common.by import By
import time

@when(u'Check Terms and Conditions text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/a").text

    if text == "I accept the Terms and Conditions":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'Click on Terms and Conditions text')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/a")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check for Terms and Conditions header on New Page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "/html/body/div[1]/h1").text

    if text == "Terms and Conditions":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check for User Eligibility text on New Page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "/html/body/div[2]/h2[1]").text

    if text == "User Eligibility":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check for Scope of Terms and Conditions text on New Page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "/html/body/div[2]/h2[2]").text

    if text == "Scope of Terms and Conditions":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check for Modifications text on New Page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "/html/body/div[2]/h2[3]").text

    if text == "Modifications":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check for Privacy Notice text on New Page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "/html/body/div[2]/h2[4]").text

    if text == "Privacy Notice":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check for Licence and Ownership text on New Page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "/html/body/div[2]/h2[5]").text

    if text == "Licence and Ownership":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check for System and Network Security text on New Page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "/html/body/div[2]/h2[6]").text

    if text == "System & Network Security":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"