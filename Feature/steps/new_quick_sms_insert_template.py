from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
new_quick_sms_insert_templateObj = CU.new_quick_sms_insert_template()

new_quick_sms_inputObj = CU.new_quick_sms_input()

@then(u'select sender Id')
def step_impl(context):
    for element_id in new_quick_sms_inputObj.new_quick_sms_input_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_quick_sms_inputObj.new_quick_sms_input_list[element_id])
        print(f"{element_id}")


@then(u'click on Insert Template')
def step_impl(context):
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)
    # context.driver.find_element(By.ID, "insert_template").click()


@then(u'Check elements are present in popup window')
def step_impl(context):
    for x in new_quick_sms_insert_templateObj.new_quick_sms_insert_template_label_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()
