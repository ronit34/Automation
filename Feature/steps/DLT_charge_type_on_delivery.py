import time
from behave import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

import Telspiel_CommonUtility as CU
TelspielChildaxisobj = CU.Telspiel_Child_axis()
Telspieltucuseridobj = CU.Telspiel_Child_axis_user()

@then(u'insert elements into given fields to add tuc')
def step_impl(context):
    #Enter Name
    time.sleep(1)
    context.driver.find_element(By.ID, "smpps").clear()

    # Click on default gateway
    button = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div[27]/div[1]/label/input")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element(By.ID, "smsapi").clear()

    time.sleep(1)
    for element_id in TelspielChildaxisobj.Telspiel_Child_axis_list.keys():

        if element_id != "cancel" and element_id != "save_tuc" and element_id != "cost_unit" and element_id != "accmgr" and element_id != "billing_type" and element_id != "dlt_charges" and element_id != "sms_charges":
            context.driver.find_element(By.ID, element_id).send_keys(
                TelspielChildaxisobj.Telspiel_Child_axis_list[element_id])
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


@then(u'insert the data into given fields to add user')
def step_impl(context):
    for element_id in Telspieltucuseridobj.Telspiel_Child_axis_user_list.keys():
        try:
            if element_id != "role_type" and element_id != "tuc" and element_id != "save_user":
                context.driver.find_element(By.ID, element_id).send_keys(Telspieltucuseridobj.Telspiel_Child_axis_user_list[element_id])

            elif element_id == "role_type":
                role_type = context.driver.find_element(By.ID, element_id)
                select = Select(role_type)

                select.select_by_value("1112")

            elif element_id == "tuc":
                tuc = context.driver.find_element(By.ID, element_id)
                select = Select(tuc)
                #28th Feb
                select.select_by_value("2005")

            else:
                button = context.driver.find_element_by_id("save_user")
                context.driver.execute_script("arguments[0].click();", button)

        except NameError:
            print(NameError)

    # Click on Create
    button = context.driver.find_element_by_id("save_user")
    context.driver.execute_script("arguments[0].click();", button)

# @then(u'Log out from the Tenant')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_xpath("//*[@id='profile']/div/p[1]")
#     context.driver.execute_script("arguments[0].click();", button)
#
#     time.sleep(1)
#     button = context.driver.find_element_by_id("log-out")
#     context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for OTP charge type option')
def step_impl(context):
    time.sleep(1)
    val1 = context.driver.find_element_by_xpath("//*[@id='otp_acc_type']/option[2]").get_attribute("value")
    val2 = context.driver.find_element_by_xpath("//*[@id='otp_acc_type']/option[3]").get_attribute("value")

    if val1 == "onsubmission" and val2 == "ondelivery":
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
    else:
        assert False, f"{val1}, {val2} ---> Parent is not on ondelivery"

@then(u'Check for Trans charge type option')
def step_impl(context):
    time.sleep(1)
    val1 = context.driver.find_element_by_xpath("//*[@id='trans_acc_type']/option[2]").get_attribute("value")
    val2 = context.driver.find_element_by_xpath("//*[@id='trans_acc_type']/option[3]").get_attribute("value")

    if val1 == "onsubmission" and val2 == "ondelivery":
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
    else:
        assert False, f"{val1}, {val2} ---> Parent is not on ondelivery"

@then(u'Check for Promo charge type option')
def step_impl(context):
    time.sleep(1)
    val1 = context.driver.find_element_by_xpath("//*[@id='promo_acc_type']/option[2]").get_attribute("value")
    val2 = context.driver.find_element_by_xpath("//*[@id='promo_acc_type']/option[3]").get_attribute("value")

    if val1 == "onsubmission" and val2 == "ondelivery":
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
    else:
        assert False, f"{val1}, {val2} ---> Parent is not on ondelivery"

@then(u'Check for Govt charge type option')
def step_impl(context):
    time.sleep(1)
    val1 = context.driver.find_element_by_xpath("//*[@id='gov_acc_type']/option[2]").get_attribute("value")
    val2 = context.driver.find_element_by_xpath("//*[@id='gov_acc_type']/option[3]").get_attribute("value")

    if val1 == "onsubmission" and val2 == "ondelivery":
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
    else:
        assert False, f"{val1}, {val2} ---> Parent is not on ondelivery"

@then(u'Check for SIM Route charge type option')
def step_impl(context):
    time.sleep(1)
    val1 = context.driver.find_element_by_xpath("//*[@id='sim_acc_type']/option[2]").get_attribute("value")
    val2 = context.driver.find_element_by_xpath("//*[@id='sim_acc_type']/option[3]").get_attribute("value")

    if val1 == "onsubmission" and val2 == "ondelivery":
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
    else:
        assert False, f"{val1}, {val2} ---> Parent is not on ondelivery"

@then(u'Check for Default charge type option')
def step_impl(context):
    time.sleep(1)
    val1 = context.driver.find_element_by_xpath("//*[@id='default_acc_type']/option[2]").get_attribute("value")
    val2 = context.driver.find_element_by_xpath("//*[@id='default_acc_type']/option[3]").get_attribute("value")

    if val1 == "onsubmission" and val2 == "ondelivery":
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
        print(f"{val1}, {val2} ---> Parent is on ondelivery")
    else:
        assert False, f"{val1}, {val2} ---> Parent is not on ondelivery"

    # time.sleep(1)
    # context.driver.close()

