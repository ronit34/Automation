from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'check label of Dashboard')
def dashboard(context):
    time.sleep(1)
    dash = context.driver.find_element(By.ID, "menu_dashboard").text
    if (dash == "Dashboard"):
        assert True, f"{dash} found"
    else:
        assert False, f"{dash} not found"


@then(u'check label of user management')
def user_management(context):
    UM = context.driver.find_element(By.ID, "menu_users").text
    if (UM == "User Management"):
        assert True, f"{UM} found"
    else:
        assert False, f"{UM} not found"


@then(u'check label Credits')
def credits(context):
    CA = context.driver.find_element(By.ID, "menu_credit_allocation").text
    if (CA == "Credits"):
        assert True, f"{CA} found"
    else:
        assert False, f"{CA} not found"

@then(u'check label of Master Balance')
def master_bal(context):
    # MB = context.driver.find_element(By.ID, "menu_master_balance").text
    MB = context.driver.find_element(By.XPATH, "//*[@id='menu_master_balance']/p").text
    # if (MB == "Master Balance"):
    if (MB == "Master Credits"):
        assert True, f"{MB} found"
    else:
        assert False, f"{MB} not found"


@then(u'check label of Master License')
def master_lic(context):
    # ML = context.driver.find_element(By.ID, "menu_master_license").text
    ML = context.driver.find_element(By.XPATH, "//*[@id='menu_master_license']/p").text
    if (ML == "Master Licenses"):
        assert True, f"{ML} found"
    else:
        assert False, f"{ML} not found"

    # time.sleep(1)
    # context.driver.close()



