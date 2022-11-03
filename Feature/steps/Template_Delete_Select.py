# import time
#
# from behave import *
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
#
# @then(u'Select Entity ID from Entity ID dropdown')
# def step_impl(context):
#     time.sleep(1)
#     ele = context.driver.find_element(By.ID, "bulktemplate_entity_id")
#     select = Select(ele)
#     select.select_by_value("123")
#
# @then(u'Select Operator from Operator dropdown')
# def step_impl(context):
#     time.sleep(1)
#     ele = context.driver.find_element(By.ID, "bulk-operator")
#     select = Select(ele)
#     select.select_by_value("vodafone")
#
# @then(u'Choose file from Choose file option')
# def step_impl(context):
#     time.sleep(1)
#     a = context.driver.switch_to.frame("up_onex_file")
#     context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/templateBulkVodafone.csv")
#     time.sleep(1)
#     context.driver.switch_to.default_content()
#
# @then(u'Click on Save Template button')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_id("bulk-save")
#     context.driver.execute_script("arguments[0].click();", button)
#
# @then(u'Click on the ok button of Message popup')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_id("ok_modal")
#     context.driver.execute_script("arguments[0].click();", button)
#
# @then(u'Select all the files of that group')
# def step_impl(context):
#     time.sleep(2)
#     checkboxes = context.driver.find_elements_by_css_selector("input[type= 'checkbox']")
#     chk = [checkbox for checkbox in checkboxes]
#     for i in chk[8:]:
#         time.sleep(1)
#         if not i.is_selected():
#             time.sleep(1)
#             i.click()
#             time.sleep(1)
#
# @then(u'Click on Delete Selected button')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_id("delete_template")
#     context.driver.execute_script("arguments[0].click();", button)
#
# @then(u'Click on the Delete button of Delete Selected popup')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_id("delete")
#     context.driver.execute_script("arguments[0].click();", button)
#
#     time.sleep(2)
#     context.driver.close()
#
