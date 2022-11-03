# from behave import *
# import time
# from selenium.webdriver.common.by import By
#
# import Tenant_CommomUtility as CU
# options_typeObj = CU.options_type()
#
#
# @then(u'Click on Type tab')
# def step_impl(context):
#     time.sleep(1)
#     context.driver.find_element(By.ID, "option_type").click()
#
#
# @then(u'Click on Add Type')
# def step_impl(context):
#     context.driver.find_element(By.ID, "add_type").click()
#
#
# @then(u'Check elements are present in Type')
# def step_impl(context):
#     for x in options_typeObj.options_type_list:
#         try:
#             status = context.driver.find_element(By.ID, x).is_displayed()
#             print(f"{x} --> is {status} ")
#         except NameError:
#             print(NameError)
#
#
# @then(u'enter data into Type')
# def step_impl(context):
#     for element_id in options_typeObj.options_type_list.keys():
#         context.driver.find_element(By.ID, element_id).send_keys(options_typeObj.options_type_list[element_id])
#         print(f"{element_id}")
#
#
# @then(u'Verify Type is added or not')
# def Type(context):
#     Type = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
#     if Type == "OTP":
#         assert True, f"Type {Type} Is Added Succesfully"
#     else:
#         assert False, f"Type {Type} Unable To Add"
#
#     time.sleep(1)
#     context.driver.close()
