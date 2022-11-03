from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


@then(u'Click on Bulk Upload')
def step_impl(context):
    context.driver.find_element(By.ID, "bulktemplate_tab").click()


@then(u'Select Entity Id')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "bulktemplate_entity_id")
    select = Select(entity)
    select.select_by_visible_text("Onextel(123)")
    # select.select_by_visible_text("OTPL(321)")

@then(u'Select operator')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "bulk-operator")
    select = Select(entity)
    # select.select_by_visible_text("Airtel")
    select.select_by_visible_text("Jio")
    # select.select_by_visible_text("Vodafone")
    # select.select_by_visible_text("Bsnl")


@then(u'Choose File')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    # context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/templateBulkAirtel.csv")
    context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/templateBulkJio.xlsx")
    # context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/templateBulkVodafone.csv")
    # context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/templateBulkBsnl.csv")

@then(u'Check for Remove file button')
def step_impl(context):
    time.sleep(1)
    context.driver.switch_to.default_content()
    time.sleep(2)
    text = context.driver.find_element_by_id("remove_file").text
    if text == "Remove File":
        assert True, "Remove file button present"
    else:
        assert False, "Remove file button absent"

@then(u'Click on reset')
def step_impl(context):
    time.sleep(1)
    context.driver.switch_to.default_content()
    time.sleep(1)
    context.driver.find_element_by_id("bulk-cancel").click()


@then(u'Click on save template')
def step_impl(context):
    time.sleep(1)
    context.driver.switch_to.default_content()
    button = context.driver.find_element_by_id("bulk-save")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on ok butn')
def step_impl(context):
    time.sleep(1)
    context.driver.switch_to.default_content()
    # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div/div/div[2]/h5").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div/div/div[2]/h5").text
    # if (text == "New Templates Added Successfully"):
    if (text == "New Templates Added Successfully !!!"):
    # if (text == "1 Templates from the file already exists !!!"):
        context.driver.find_element_by_id("ok_modal").click()
    else:
        assert False, "Text Failed"

    # time.sleep(1)
    # context.driver.close()