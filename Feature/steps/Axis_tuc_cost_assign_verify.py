import time
from behave import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

import Telspiel_CommonUtility as CU
AxisChildobj = CU.Axis_Child_axischild_less_cost()
AxisChildobj1 = CU.Axis_Child_axischild_update_cost()

@then(u'insert lss cost and check error label')
def step_impl(context):
    # Enter Name
    time.sleep(1)
    context.driver.find_element(By.ID, "smpps").clear()

    time.sleep(1)
    context.driver.find_element(By.ID, "smsapi").clear()

    time.sleep(1)
    for element_id in AxisChildobj.Axis_Child_axischild_list.keys():

        if element_id != "cancel" and element_id != "save_tuc" and element_id != "cost_unit" and element_id != "accmgr" and element_id != "billing_type" and element_id != "dlt_charges" and element_id != "sms_charges":
            context.driver.find_element(By.ID, element_id).send_keys(
                AxisChildobj.Axis_Child_axischild_list[element_id])
        elif element_id == "cost_unit":
            cu = context.driver.find_element(By.ID, element_id)
            select = Select(cu)

            select.select_by_visible_text("Paisa")

        elif element_id == "accmgr":
            accmgr = context.driver.find_element(By.ID, element_id)
            select = Select(accmgr)

            select.select_by_visible_text("sant")

        elif element_id == "billing_type":
            billing_type = context.driver.find_element(By.ID, element_id)
            select = Select(billing_type)
            select.select_by_visible_text("POSTPAID")

        elif element_id == "dlt_charges":
            dlt_charges = context.driver.find_element(By.ID, element_id)
            select = Select(dlt_charges)
            select.select_by_visible_text("On Delivery")

        elif element_id == "sms_charges":
            sms_charges = context.driver.find_element(By.ID, element_id)
            select = Select(sms_charges)
            select.select_by_visible_text("On Delivery")

        elif element_id == "mask_phone":
            mask_phone = context.driver.find_element(By.ID, element_id)
            select = Select(mask_phone)
            select.select_by_visible_text("Yes")

@then(u'check error label of cost')
def step_impl(context):
    time.sleep(1)
    otp = context.driver.find_element(By.ID, "cost_per_otppanel1").text
    if otp == "Cost For OTP* can't be less than : 10":
        print(f"{otp} -----> verified")
        # print(f"{otp} -----> verified")
    else:
        assert False , print(f"{otp}  ---> not present")


    trans = context.driver.find_element(By.ID, "cost_per_txpanel1").text
    if trans == "Cost For Transactional* can't be less than : 60":
        print(f"{trans} -----> verified")
        # assert True, print(f"{trans} -----> verified")
    else:
        assert False , print(f"{trans}  ---> not present")


    promo = context.driver.find_element(By.ID, "cost_per_promopanel1").text
    if promo == "Cost For Promotional* can't be less than : 30":
        print(f"{promo} -----> verified")
        # assert True, print(f"{promo} -----> verified")
    else:
        assert False , print(f"{promo}  ---> not present")


    sim_route = context.driver.find_element(By.ID, "cost_per_simroutepanel1").text
    if sim_route == "Cost For Sim Route* can't be less than : 40":
        print(f"{sim_route} -----> verified")
        # print(f"{sim_route} -----> verified")
    else:
        assert False , print(f"{otp}  ---> not present")


    scrub = context.driver.find_element(By.ID, "scrubbing_costpanel1").text
    if scrub == "Scrubbing Cost Per SMS* can't be less than : 40":
         print(f"{scrub} -----> verified")
         print(f"{scrub} -----> verified")
    else:
        assert False , print(f"{scrub}  ---> not present")

@then(u'update cost')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "cost_per_otp").clear()
    context.driver.find_element(By.ID, "cost_per_tx").clear()
    context.driver.find_element(By.ID, "cost_per_promo").clear()
    context.driver.find_element(By.ID, "cost_per_simroute").clear()
    context.driver.find_element(By.ID, "scrubbing_cost").clear()

    time.sleep(2)
    for element_id in AxisChildobj1.Axis_Child_axischild_new_cost_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(AxisChildobj1.Axis_Child_axischild_new_cost_list[element_id])
