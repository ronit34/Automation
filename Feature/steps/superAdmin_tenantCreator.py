import time
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.support.wait import WebDriverWait

import CommonUtility as CU

tenantcreatorObj = CU.tenant_creator()

# tenant_creator_dropdownObj = CU.tenant_creator_dropdown()

@then(u'Click on Terms And Conditions Check Box')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").click()


@then(u'Click on Sign in Button')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element( By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click on User_Management')
def User_Management(context):
    time.sleep(2)
    context.driver.implicitly_wait(10)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_users']/p")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Check Add tenant button present')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.ID, "create_tenant").is_displayed()

@then(u'Click on Add Tenants button')
def Add_Button(context):

    context.driver.find_element(By.ID, "create_tenant").click()

@then(u'check all element present')
def step_impl(context):

    for element_id in tenantcreatorObj.tenant_creator_inputbox_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
        except NameError:
            print(NameError)

    # for element_id in tenant_creator_dropdownObj.tenant_creator_dropdown_inputbox_list.keys():
    #     try:
    #         status = context.driver.find_element(By.ID, element_id).is_displayed()
    #         print(f"{element_id} --> is {status} ")
    #     except NameError:
    #         print(NameError)



@then(u'insert details')
def step_impl(context):

        for element_id in tenantcreatorObj.tenant_creator_inputbox_list.keys():
            context.driver.find_element(By.ID, element_id).send_keys(
                tenantcreatorObj.tenant_creator_inputbox_list[element_id])
            print(f"{element_id}")

    # for element_id in tenant_creator_dropdownObj.tenant_creator_dropdown_inputbox_list.keys():
    #     context.driver.find_element(By.ID, element_id).send_keys(
    #         tenant_creator_dropdownObj.tenant_creator_dropdown_inputbox_list[element_id])
    #     print(f"{element_id}")
@then(u'click create')
def step_impl(context):

    button = context.driver.find_element( By.ID, "save_tenant")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check Tenant created succussfully or not')
def tenant(context):
    time.sleep(1)
    tenant = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if (tenant == "Onexmedia(10)"):
        assert True, f"{tenant} found"
    else:
        assert False, f"{tenant} not found"

    # time.sleep(1)
    # context.driver.close()
