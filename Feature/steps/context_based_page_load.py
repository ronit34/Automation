from behave import *

from selenium.webdriver.common.by import By

import CommonUtility as CU

page_loadObj = CU.page_load()

page_idObj = CU.page_id()

page_tenant_idObj = CU.page_tenant_id()

page_tuc_idObj = CU.page_tuc_id()


@then(u'check all pages')
def step_impl(context):
     loginintoContext(context, "onexsa", "onexsa", page_loadObj.list_onexsa, page_idObj.page_id_onexsa_list)
     print("Super Admin Login")
     input("Super Admin Logged In")

     loginintoContext(context, "Onexadmin", "ali", page_loadObj.list_tenant, page_tenant_idObj.page_id_tenant_list)
     print("Tenant Login")
     input("Tenant Logged In")

     loginintoContext(context, "ICICIAdmin", "ali", page_loadObj.list_tuc, page_tuc_idObj.page_id_tuc_list)
     print("TUC Login")
     input("TUC Logged In")
def loginintoContext(context, username, password, list_pages, list_hyperlinks):
    context.driver.get("http://localhost:8000/index")
    context.driver.find_element(By.ID, "email").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.implicitly_wait(500)
    # check box
    context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").click()
    context.driver.implicitly_wait(500)
    # login button press
    button = context.driver.find_element(By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)
    input("Press Enter to continue...")

    for x in list_pages:
        context.driver.get(x)
        print(f" in page --->{x}")
        for y in list_hyperlinks:

            pagelink = context.driver.find_element(By.ID, y)
            context.driver.execute_script("arguments[0].click();", pagelink)


        input("Press click to continue")

