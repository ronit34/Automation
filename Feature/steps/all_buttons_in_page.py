from behave import *
from selenium.webdriver.common.by import By
import time
import all_in_one
import CommonUtility as CU
loginObj = CU.login()
serverAdd = "http://localhost:8000/index"
creditaddObj = CU.credit_add()

creditallocationObj = CU.credit_allocation()
credit_allocation_labelObj = CU.credit_allocation_label()

@then(u'try all in one code')
def step_impl(context):
    loginintoContext(context, "onexsa", "onexsa", loginObj.User_logins)
    all_in_one.masterbalance(context, "10000")
    # credit_allocation(context,"1000")

def loginintoContext(context, username, password, login):
    context.driver.get(serverAdd)
    context.driver.find_element(By.ID, "email").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.implicitly_wait(500)
    # check box
    context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").click()
    context.driver.implicitly_wait(500)
    # login button press
    button = context.driver.find_element(By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)


#
# def credit_allocation(context,credit):
#     time.sleep(1)
#     context.driver.find_element(By.ID, "menu_credit_allocation").click()
#
#     #********************** Code for checking credit allocation elements and labels are present*******************
#     for x in creditallocationObj.credit_allocation_inputbox_list:
#         try:
#             status = context.driver.find_element(By.ID, x).is_displayed()
#             print(f"{x} --> is {status} ")
#         except NameError:
#             print(NameError)
#
#     for x in credit_allocation_labelObj.credit_allocation_label_inputbox_list:
#         context.driver.implicitly_wait(20)
#         if context.driver.find_element(By.ID, x).text == credit_allocation_labelObj.credit_allocation_label_inputbox_list[x]:
#             print(f"{credit_allocation_labelObj.credit_allocation_label_inputbox_list[x]}--> found")
#         else:
#             print(f"{credit_allocation_labelObj.credit_allocation_label_inputbox_list[x]}--> Not found")
#
#     context.driver.find_element(By.ID, "update_credit").click()
#     #***************** Code for checking update credit elements are present*****************
#     for x in creditaddObj.credit_add_inputbox_list:
#         try:
#             status = context.driver.find_element(By.ID, x).is_displayed()
#             print(f"{x} --> is {status} ")
#         except NameError:
#             print(NameError)
#
#     context.driver.find_element(By.ID, "select_tuc").click()
#     context.driver.find_element(By.XPATH, "//*[@id='select_tuc']/option[2]").click()
#     context.driver.find_element(By.XPATH, "//*[@id='add_credit_div']/label").click()
#     context.driver.find_element(By.ID, "credits_amount").send_keys(credit)
#     context.driver.find_element(By.XPATH, "//*[@id='update_credits']").click()

