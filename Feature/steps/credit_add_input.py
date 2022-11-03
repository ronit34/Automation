import time
from behave import *
from selenium.webdriver.common.by import By

@then(u'Select TUC')
def select_tuc(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "select_tuc").click()
    context.driver.find_element(By.XPATH, "//*[@id='select_tuc']/option[2]").click()

@then(u'Select Add-Credit')
def select_add(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='add_credit_div']/label")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Enter the Amount "{amount}"')
def enter_amt(context,amount):
    time.sleep(1)
    context.driver.find_element(By.ID, "credits_amount").send_keys(amount)

@then(u'Click on update for transaction')
def click_update(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "update_credits").click()

@then(u'check credit added successfully')
def step_impl(context):
    time.sleep(3)
    credit = context.driver.find_element(By.XPATH, "//*[@id='campaign-table']/tbody/tr[2]/td[3]").text
    if (credit == "2,00,000"):
        assert True, f"{credit} found"
    else:
        assert False, f"{credit} not found"

    # time.sleep(1)
    # context.driver.close()