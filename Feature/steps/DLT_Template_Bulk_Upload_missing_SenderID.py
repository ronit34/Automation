from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

@then(u'Select bsnl operator')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "bulk-operator")
    select = Select(entity)
    select.select_by_visible_text("Bsnl")

@then(u'choose file for bsnl')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/templateBulkBsnl.csv")


@then(u'check senderid Field missing popup')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/h5").text
    if text == "One or more Header/SenderID are empty!! Please Check File!!":
        assert True, f"{text} -----> present"
    else:
        assert False, f"{text} -----> absent"


@then(u'click on OK button in bulk upload')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_id("ok_modal").click()

