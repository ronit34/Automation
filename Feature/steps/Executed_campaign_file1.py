from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import CommonUtility as CU
DLT_templateIDObj = CU.DLT_templateID_executed()
DLT_templateID_dropdownobj=CU.DLT_templateID_dropdown()

executed_campaign_inputObj = CU.executed_campaign_input()


@then(u'Enter data to template fields')
def step_impl(context):
    for element_id in DLT_templateIDObj.DLT_templateID_executed_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            DLT_templateIDObj.DLT_templateID_executed_inputbox_list[element_id])
        print(f"{element_id}")


    for element_id in DLT_templateID_dropdownobj.DLT_templateID_dropdown_inputbox_list.keys():
        try:
            context.driver.implicitly_wait(20)
            element_obj = context.driver.find_element(By.ID, element_id)
            context.driver.implicitly_wait(20)
            select = Select(element_obj)
            context.driver.implicitly_wait(20)
            select.select_by_visible_text(DLT_templateID_dropdownobj.DLT_templateID_dropdown_inputbox_list[element_id])

        except NameError:
            print(NameError)

    time.sleep(2)
    entity = context.driver.find_element(By.ID, "template_sender_id")
    select = Select(entity)
    select.select_by_visible_text("098765")


@then(u'insert data to schedule quick sms')
def step_impl(context):
    for element_id in executed_campaign_inputObj.executed_campaign_input_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            executed_campaign_inputObj.executed_campaign_input_list[element_id])
        print(f"{element_id}")

    # click on Insert Template template_name
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("serv_imp")

    # select template as English short
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("executed campaign")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check sms scheduled for execution')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr[2]/td[1]").text
    if text == "098765":
        print(f"{text}-----> campaign scheduled")
    else:
        assert False, f"{text}-----------> campaign not scheduled"

    # time.sleep(2)
    # context.driver.close()

