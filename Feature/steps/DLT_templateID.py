from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import CommonUtility as CU

DLT_templateIDObj = CU.DLT_templateID()
DLT_templateID_dropdownobj=CU.DLT_templateID_dropdown()

@then(u'click on template')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "template_tab").click()

@then(u'click on Add template id button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID,"create_template")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check elements is present on the template page')
def step_impl(context):
    for x in DLT_templateIDObj.DLT_templateID_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

    for element_id in DLT_templateID_dropdownobj.DLT_templateID_dropdown_inputbox_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")

        except NameError:
            print(NameError)

@then(u'Enter the data into templateid fields')
def step_impl(context):
    for element_id in DLT_templateIDObj.DLT_templateID_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            DLT_templateIDObj.DLT_templateID_inputbox_list[element_id])
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
    select.select_by_visible_text("123456")

@then(u'Click on template Add')
def step_impl(context):

    context.driver.find_element(By.ID, "add_template").click()

@then(u'Check Template is created or not')
def template(context):
    time.sleep(1)
    # template = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[1]").text
    template = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[2]").text
    if (template == "English Long"):
        assert True, f"{template} found"
    else:
        assert False, f"{template} not found"

    # time.sleep(1)
    # context.driver.close()









