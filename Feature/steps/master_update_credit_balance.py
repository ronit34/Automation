from behave import *
import time
from selenium.webdriver.common.by import By
import CommonUtility as CU

loginObj = CU.login()
master_update_credit_balanceObj = CU.master_update_credit_balance()
serverAddress = "http://localhost:8000/index"

@then(u'do the master_update_credit_balance all steps')
def step_impl(context):
    loginintoContext(context, "onexsa", "onexsa", loginObj.User_logins)
    master_update_credit_balance(context,"1000")

#--------------------------------------------------------------------------------


def loginintoContext(context, username, password, login):
    context.driver.maximize_window()
    context.driver.get(serverAddress)
    context.driver.find_element(By.ID, "email").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.implicitly_wait(500)
    # check box
    context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").click()
    context.driver.implicitly_wait(500)
    # login button press
    button = context.driver.find_element(By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)

def master_update_credit_balance(context, amount):
    for x in master_update_credit_balanceObj.master_update_credit_balance_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == master_update_credit_balanceObj.master_update_credit_balance_list[x]:
            print(f"{master_update_credit_balanceObj.master_update_credit_balance_list[x]}--> Aailable Credit is 0 ")
        else:
            print(f"{master_update_credit_balanceObj.master_update_credit_balance_list[x]}--> Not found")

    context.driver.find_element(By.ID, "menu_master_balance").click()
    context.driver.find_element(By.ID, "update_balance").click()
    context.driver.find_element(By.ID, "amount").send_keys(amount)
    context.driver.find_element(By.ID, "add").click()

    print(f"Added Balance is :{amount} ")


