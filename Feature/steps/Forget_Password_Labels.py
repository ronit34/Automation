from behave import *
import time

@then(u'Check text of error message')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='errormsg']/span").text
    if text == "Invalid UserName or Password":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Forget Password text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div/div/div[2]/div[2]/a").text
    if text == "Forgot Password ?":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"


@then(u'Click on Forget Password')
def step_impl(context):
    time.sleep(1)
    if context.driver.find_element_by_xpath("//*[@id='errormsg']/span").text == \
            "Invalid UserName or Password":
        button = context.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/a")
        context.driver.execute_script("arguments[0].click();", button)


@then(u'Check text of Forget Password')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div/div/div[2]/p[3]").text
    if text == "Forgot Password":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"


@then(u'Check description text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div/div/div[2]/p[5]").text
    if text == "A link will be sent to the associated e-mail.":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"


@then(u'Check text of Reset Password button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("send_email").text
    if text == "Reset Password":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"