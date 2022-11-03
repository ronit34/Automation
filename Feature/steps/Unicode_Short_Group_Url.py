import re
from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import CommonUtility as CU
new_quick_sms_inputObj1 = CU.new_quick_sms_input_no_recipients()


@then(u'insert data into fields without recipients')
def step_impl(context):
    for element_id in new_quick_sms_inputObj1.new_quick_sms_input_no_recipients_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_quick_sms_inputObj1.new_quick_sms_input_no_recipients_list[element_id])
        print(f"{element_id}")


