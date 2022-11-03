import time
from behave import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

import TUC_CommonUtility as CU
Sales_child_loanobj = CU.Sales_child_loan()

@then(u'Enter Username "sales" and password "sales"')
def step_impl(context):
    context.driver.find_element_by_id("email").send_keys("sales")
    context.driver.find_element_by_id("password").send_keys("sales")

@then(u'check elements are present in add tuc of sales')
def step_impl(context):
    for element_id in Sales_child_loanobj.Sales_child_loan_list.keys():
        try:
            time.sleep(1)
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'insert elements in add tuc of sales')
def isert_elements(context):
    time.sleep(1)
    context.driver.find_element(By.ID,"smpps").clear()

    time.sleep(1)
    context.driver.find_element(By.ID, "smsapi").clear()

    time.sleep(1)
    for element_id in Sales_child_loanobj.Sales_child_loan_list.keys():

            if element_id != "cancel" and element_id != "save_tuc" and element_id != "cost_unit" and element_id != "accmgr" and element_id != "billing_type" and element_id != "dlt_charges" and element_id != "sms_charges":
                context.driver.find_element(By.ID, element_id).send_keys(Sales_child_loanobj.Sales_child_loan_list[element_id])

            elif element_id == "otp_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "trans_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "promo_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "gov_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "sim_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "default_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "cost_unit":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("Paisa")

            # elif element_id == "accmgr":
            #     accmgr = context.driver.find_element(By.ID, element_id)
            #     select = Select(accmgr)
            #     select.select_by_visible_text("sant")

            elif element_id == "billing_type":
                billing_type = context.driver.find_element(By.ID, element_id)
                select = Select(billing_type)
                select.select_by_visible_text("POSTPAID")

            # elif element_id == "dlt_charges":
            #     dlt_charges = context.driver.find_element(By.ID, element_id)
            #     select = Select(dlt_charges)
            #     select.select_by_visible_text("On Delivery")
            #
            # elif element_id == "sms_charges":
            #     sms_charges = context.driver.find_element(By.ID, element_id)
            #     select = Select(sms_charges)
            #     select.select_by_visible_text("On Delivery")

            elif element_id == "mask_phone":
                mask_phone = context.driver.find_element(By.ID, element_id)
                select = Select(mask_phone)
                select.select_by_visible_text("Yes")

        # except NameError:
        #     print(NameError)

@then(u'check tuc is created in sales tuc')
def step_impl(context):
    time.sleep(1)
    tuc=context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if(tuc=="CREDIT"):
        print(f"{tuc} Created Successfully")
    else:
        print(f"{tuc} IS Not Created")

    # time.sleep(1)
    # context.driver.close()
