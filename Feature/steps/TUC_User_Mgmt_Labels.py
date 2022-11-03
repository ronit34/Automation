from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

@then(u'Check label of User Management in header')
def step_impl(context):
    V1 = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if V1 == "User Management":
        assert True, f"{V1} is present"
    else:
        assert False, f"{V1} is not present"

@then(u'Check for TUC tab')
def step_impl(context):
    V1 = context.driver.find_element_by_id("tuc_view").text
    if V1 == "TUC":
        context.driver.find_element_by_id("tuc_view").click()
    else:
        assert False, f"{V1} is not present"

@then(u'Click on Add TUC')
def step_impl(context):
    time.sleep(1)
    V2 = context.driver.find_element_by_id("create_tuc").text
    # if V2 == "+Add TUC":
    if V2 == "+ Add TUC":
        time.sleep(2)
        context.driver.find_element_by_id("create_tuc").click()
    else:
        assert False, f"{V2} is not present"

@then(u'Check for Add Tenant Customer Logo')
def step_impl(context):
    V3 = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if V3 == "Add Tenant Customer":
        assert True, f"{V3} is present"
    else:
        assert False, f"{V3} is not present"

@then(u'Check for TUC Info')
def step_impl(context):
    V4 = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[1]/h5").text
    if V4 == "Tuc Info":
        assert True, f"{V4} is present"
    else:
        assert False, f"{V4} is not present"

@then(u'Check for Name')
def step_impl(context):
    V5 = context.driver.find_element_by_xpath("//*[@id='namepanel1']").text
    if V5 == "Name*":
        assert True, f"{V5} is present"
    else:
        assert False, f"{V5} is not present"

@then(u'Check for Cost For OTP')
def step_impl(context):
    V6 = context.driver.find_element_by_id("cost_per_otppanel1").text
    if V6 == "Cost For OTP*":
        assert True, f"{V6} is present"
    else:
        assert False, f"{V6} is not present"

@then(u'Check for Transactional')
def step_impl(context):
    V7 = context.driver.find_element_by_id("cost_per_txpanel1").text
    if V7 == "Cost For Transactional*":
        assert True, f"{V7} is present"
    else:
        assert False, f"{V7} is not present"

@then(u'Check for Cost For Promotional')
def step_impl(context):
    V8 = context.driver.find_element_by_id("cost_per_promopanel1").text
    if V8 == "Cost For Promotional*":
        assert True, f"{V8} is present"
    else:
        assert False, f"{V8} is not present"

@then(u'Check For Cost For Sim Route')
def step_impl(context):
    V9 = context.driver.find_element_by_id("cost_per_simroutepanel1").text
    if V9 == "Cost For Sim Route*":
        assert True, f"{V9} is present"
    else:
        assert False, f"{V9} is not present"

@then(u'Check for Scrubbing Cost Per SMS')
def step_impl(context):
    V10 = context.driver.find_element_by_id("scrubbing_costpanel1").text
    if V10 == "Scrubbing Cost Per SMS*":
        assert True, f"{V10} is present"
    else:
        assert False, f"{V10} is not present"

@then(u'Govt SMS Cost')
def step_impl(context):
    V11 = context.driver.find_element_by_id("govt_sms_costpanel1").text
    if V11 == "Govt. SMS Cost":
        assert True, f"{V11} is present"
    else:
        assert False, f"{V11} is not present"

@then(u'Govt Scrubbing Cost')
def step_impl(context):
    V12 = context.driver.find_element_by_id("govt_scrubbing_costpanel1").text
    if V12 == "Govt. Scrubbing Cost":
        assert True, f"{V12} is present"
    else:
        assert False, f"{V12} is not present"

@then(u'Check for Cost Unit')
def step_impl(context):
    V13 = context.driver.find_element_by_id("cost_unitpanel1").text
    if V13 == "Cost Unit*":
        assert True, f"{V13} is present"
    else:
        assert False, f"{V13} is not present"

@then(u'Check for OTP Charge type')
def step_impl(context):
    V13 = context.driver.find_element_by_id("otp_acc_typepanel1").text
    if V13 == "OTP Charges Type*":
        assert True, f"{V13} is present"
    else:
        assert False, f"{V13} is not present"

@then(u'Check for Trans Charge type')
def step_impl(context):
    V13 = context.driver.find_element_by_id("trans_acc_typepanel1").text
    if V13 == "Trans Charges Type*":
        assert True, f"{V13} is present"
    else:
        assert False, f"{V13} is not present"

@then(u'Check for Promo Charge type')
def step_impl(context):
    V13 = context.driver.find_element_by_id("promo_acc_typepanel1").text
    if V13 == "Promo Charges Type*":
        assert True, f"{V13} is present"
    else:
        assert False, f"{V13} is not present"

@then(u'Check for Govt Charge type')
def step_impl(context):
    V13 = context.driver.find_element_by_id("gov_acc_typepanel1").text
    if V13 == "Govt. Charges Type*":
        assert True, f"{V13} is present"
    else:
        assert False, f"{V13} is not present"

@then(u'Check for SIM Route Charge type')
def step_impl(context):
    V13 = context.driver.find_element_by_id("sim_acc_typepanel1").text
    if V13 == "SIM Route Charges Type*":
        assert True, f"{V13} is present"
    else:
        assert False, f"{V13} is not present"

@then(u'Check for Default Charge type')
def step_impl(context):
    V13 = context.driver.find_element_by_id("default_acc_typepanel1").text
    if V13 == "Default Charges Type*":
        assert True, f"{V13} is present"
    else:
        assert False, f"{V13} is not present"

@then(u'Check for Account Manager')
def step_impl(context):
    V14 = context.driver.find_element_by_id("accmgrpanel1").text
    if V14 == "Account Manager*":
        assert True, f"{V14} is present"
    else:
        assert False, f"{V14} is not present"

@then(u'Check for Billing Type')
def step_impl(context):
    V15 = context.driver.find_element_by_id("billing_typepanel1").text
    if V15 == "Billing Type*":
        assert True, f"{V15} is present"
    else:
        assert False, f"{V15} is not present"

@then(u'Check for DLT Charges Type')
def step_impl(context):
    V16 = context.driver.find_element_by_id("dlt_chargespanel1").text
    if V16 == "DLT Charges Type*":
        assert True, f"{V16} is present"
    else:
        assert False, f"{V16} is not present"

@then(u'Check for SMS Charges Type')
def step_impl(context):
    V17 = context.driver.find_element_by_id("sms_chargespanel1").text
    if V17 == "SMS Charges Type*":
        assert True, f"{V17} is present"
    else:
        assert False, f"{V17} is not present"

@then(u'Check for validity')
def step_impl(context):
    V17 = context.driver.find_element_by_id("validitypanel1").text
    if V17 == "Validity*":
        assert True, f"{V17} is present"
    else:
        assert False, f"{V17} is not present"

@then(u'Check for Mask Phone')
def step_impl(context):
    V17 = context.driver.find_element_by_id("mask_phonepanel1").text
    if V17 == "Mask Phone*":
        assert True, f"{V17} is present"
    else:
        assert False, f"{V17} is not present"

@then(u'Check For License')
def step_impl(context):
    time.sleep(2)
    # V1 = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[22]/h5").text
    V1 = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[28]/h5").text
    if V1 == "Licenses":
        assert True, f"{V1} is present"
    else:
        assert False, f"{V1} is not present"

@then('Check for Child TUC')
def step_impl(context):
    V1 = context.driver.find_element_by_id("childtucpanel1").text
    if V1 == "Child TUC* (88)":
        assert True, f"{V1} is present"
    else:
        assert False, f"{V1} is not present"


@then('Check for SMPPS')
def step_impl(context):
    V1 = context.driver.find_element_by_id("smppspanel1").text
    # if V1 == "SMPPS* (90)":
    if V1 == "SMPPS* (89)":
        assert True, f"{V1} is present"
    else:
        assert False, f"{V1} is not present"


@then(u'Check for SMS API tab')
def step_impl(context):
    V1 = context.driver.find_element_by_id("smsapipanel1").text
    # if V1 == "SMS API* (90)":
    if V1 == "SMS API* (84)":
    # if V1 == "SMS API* (89)":
        assert True, f"{V1} is present"
    else:
        assert False, f"{V1} is not present"

@then(u'Check for Create Button')
def step_impl(context):
    V1 = context.driver.find_element_by_id("save_tuc").get_attribute("value")
    if V1 == "Create":
        assert True, f"{V1} is present"
    else:
        assert False, f"{V1} is not present"

@then(u'Check for Cancel Button')
def step_impl(context):
    V1 = context.driver.find_element_by_id("cancel").get_attribute("value")
    if V1 == "Cancel":
        time.sleep(1)
        button = context.driver.find_element_by_xpath("//*[@id='cancel']")
        context.driver.execute_script("arguments[0].click();", button)
    else:
        assert False, f"{V1} is not present"

    # time.sleep(1)
    # context.driver.close()
