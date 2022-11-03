import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import CommonUtility as CU
new_dynamic_smsObj = CU.new_dynamic_sms()


@then(u'select sender Id and campaign')
def step_impl(context):
    # for element_id in new_dynamic_smsObj.new_dynamic_sms_input.keys():
    #     context.driver.find_element(By.ID, element_id).send_keys(
    #         new_dynamic_smsObj.new_dynamic_sms_input[element_id])
    #     print(f"{element_id}")
    campaign = context.driver.find_element(By.ID, "campaign_name")
    select = Select(campaign)
    select.select_by_visible_text("RCF(2201)")

    time.sleep(1)
    sender = context.driver.find_element(By.ID, "sender_id")
    select = Select(sender)
    select.select_by_value("123456")

