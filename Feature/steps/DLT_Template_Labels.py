from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on template tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("template_tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Template Name text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("// *[ @ id = 'template_table'] / tbody / tr[1] / th[2]").text

    if text == "Template Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if SenderID text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[1]/th[3]").text

    if text == "SenderID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if EntityID text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[1]/th[4]").text

    if text == "Entity ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if TemplateID text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[1]/th[5]").text

    if text == "Template ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Content text is present or not in dlt template')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[1]/th[6]").text

    if text == "Content":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if added on text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[1]/th[7]").text

    if text == "added on":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Type text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[1]/th[8]").text

    if text == "Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action text is present or not in dlt template')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[1]/th[9]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on add template button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("create_template")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Add Template text inside add template is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[1]/p[1]").text

    if text == "Add Template":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Template Name text inside add template is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[1]/label").text

    if text == "Template Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Template ID text inside add template is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[2]/label").text

    if text == "Template ID*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Select Type text inside add template is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[3]/label").text

    if text == "Select Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Select Entity ID text inside add template is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[4]/label").text

    if text == "Select Entity ID*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Select Sender ID text inside add template is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[5]/label").text

    if text == "Select Sender ID*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Description text inside add template is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[6]/label").text

    if text == "Description":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Content text inside add template is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[7]/label").text

    if text == "Content*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()