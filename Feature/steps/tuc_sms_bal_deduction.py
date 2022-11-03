import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import CommonUtility as CU
import new_quick_sms_input

TUC_SMS_Balance_Deductionobj = CU.TUC_SMS_Balance_Deduction()

@then(u'first check available credits')
def step_impl(context):
    time.sleep(1)
    credit=context.driver.find_element_by_id('available_credits').text
    print(f"Available credit Is={credit}")
    print(context.driver.find_element_by_id("current_date").text)

    context.driver.find_element(By.ID, "newSms").click()

    new_quick_sms_input.quick_sms(context)
    time.sleep(5)
    Updated_Available_credit=context.driver.find_element_by_id('available_credits').text
    print(f"Available credit Is={Updated_Available_credit}")
    z = int(credit.replace(',', ''))
    x = int(Updated_Available_credit.replace(',', ''))
    # z=int(credit)
    # x=int(Updated_Available_credit)
    p=int(z-x)

    ################# Wallet Updated ################
    # time.sleep(4)
    # if (p==3):
    #     print(f"Balance is deducted as per cost applied and Updated Available Credit Is = {Updated_Available_credit}")
    #     print(f"Balance is deducted as per cost applied and Updated Available Credit Is = {Updated_Available_credit}")
    # elif (p==2):
    #     print(f"One message failed and Updated Available Credit Is = {Updated_Available_credit}")
    #     print(f"One message failed and Updated Available Credit Is = {Updated_Available_credit}")
    # elif (p==1):
    #     print(f"Two messages failed and Updated Available Credit Is = {Updated_Available_credit}")
    #     print(f"Two messages failed and Updated Available Credit Is = {Updated_Available_credit}")
    # elif (p==0):
    #     print(f"All messages failed and Updated Available Credit Is = {Updated_Available_credit}")
    #     print(f"All messages failed and Updated Available Credit Is = {Updated_Available_credit}")
    # else:
    #     assert False, f" not credited as per cost"

    # time.sleep(1)
    # context.driver.close()