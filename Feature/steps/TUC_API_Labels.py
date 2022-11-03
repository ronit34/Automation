import time
from behave import *

@then(u'click on the api tab')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element_by_xpath("//*[@id='menu_api']/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if API text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if text == "API":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Key text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[2]").text
    if text == "Key":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Account Type text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[3]").text
    if text == "Account Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Password text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[4]").text
    if text == "Password":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Description text is present or not in api')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[5]").text
    if text == "Description":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Status text is present or not in api tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[6]").text
    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action text is present or not in api tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[7]").text
    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Generate api button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/a").text
    if text == "+ Generate API":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on Generate api button')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[2]/a")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Select Account Type of API text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if text == "API":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Account Type text in pop up is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if text == "API":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Description text in pop up is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if text == "API":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Send DLR text in pop up is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if text == "API":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Submit text button text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if text == "API":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if cancel button text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if text == "API":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()
