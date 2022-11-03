# import time
#
# from behave import *
# from selenium.webdriver.common.by import By
# import CommonUtility as CU
# tenantuserobj = CU.tenant_change_password()
# @then(u'Click on change password')
# def step_impl(context):
#     context.driver.implicitly_wait(10)
#     context.driver.find_element_by_id("change-password").click()
#
# @then(u'Enter details in current ,new and re-enter password fields')
# def step_impl(context):
#     time.sleep(1)
#     for element_id in tenantuserobj.tenant_change_password_inputbox_list.keys():
#      context.driver.find_element(By.ID, element_id).send_keys(
#         tenantuserobj.tenant_change_password_inputbox_list[element_id])
#      print(f"{element_id}")
#
# @then(u'Click on submit request button')
# def step_impl(context):
#     context.driver.implicitly_wait(10)
#     context.driver.find_element_by_id("change-num-email").click()
#
# @then(u'Check Successfully changed Password for Telspiel message is displayed')
# def step_impl(context):
#     status = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/div/div/div/div/div[2]/h5").is_displayed()
#     assert status is True
#     print(f"{status}:message is displayed in popup")
#
# @then(u'Click on ok')
# def step_impl(context):
#     context.driver.implicitly_wait(10)
#     context.driver.find_element_by_id("ok_modal").click()
#
#     time.sleep(1)
#     context.driver.close()