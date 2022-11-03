from behave import *
from selenium.webdriver.common.by import By
import CommonUtility as CU

page_loadObj = CU.page_load()

page_idObj = CU.page_id()

page_tenant_idObj = CU.page_tenant_id()
@then(u'check log_in_out for all pages')
def step_impl(context):
    log_in_out(context, "onexsa", "onexsa",page_loadObj.list_onexsa)

    # log_in_out(context, "Onexadmin", "ali", page_loadObj.list_tenant)

    # log_in_out(context, "ICICIAdmin", "ali", page_loadObj.list_tuc)


def log_in_out(context, username, password, list_pages):
    for x in list_pages:
        context.driver.get(x)

    #Entering Username and password
        context.driver.find_element(By.ID, "email").send_keys(username)
        context.driver.find_element(By.ID, "password").send_keys(password)

    # check box
        context.driver.implicitly_wait(100)
        context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").click()


    # login button press
        context.driver.implicitly_wait(100)
        button = context.driver.find_element(By.ID, "login_button")
        context.driver.execute_script("arguments[0].click();", button)

    # Log Out from profile
        context.driver.implicitly_wait(100)
        button = context.driver.find_element(By.ID, "dropdown-caret")
        context.driver.execute_script("arguments[0].click();", button)
        # context.driver.find_element(By.ID, "dropdown-caret").click()
        input(f"Log in to page ...{x}")
        context.driver.implicitly_wait(100)
        button = context.driver.find_element(By.XPATH, "//*[@id='profiledropdown']/li[4]/a")
        context.driver.execute_script("arguments[0].click();", button)
        input(f"Log Out from page ...{x}")
