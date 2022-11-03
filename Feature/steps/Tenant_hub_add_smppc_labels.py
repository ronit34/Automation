from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'check text of Name*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='namepanel1']").text

    if text == "Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of  add smppc Carrier Name*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='carrier_idpanel1']").text

    if text == "Carrier Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of smppc Vendor name')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("vendorpanel1").text

    if text == "Vendor Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of add smppc account type')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("accounttypepanel1").text

    if text == "Account Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of  add smppc Circle Name*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='circle_idpanel1']").text

    if text == "Circle Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Gateway Id*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='gateway_idpanel1']").text

    if text == "Gateway Id*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of SMPP LoginId*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='smpploginpanel1']").text

    if text == "SMPP LoginId*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of System ID*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='usernamepanel1']").text

    if text == "System ID*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Password*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='passwordpanel1']").text

    if text == "Password*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Primary Host/IP*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='hostpanel1']").text

    if text == "Primary Host/IP*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Secondary Host/IP')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id(
        "host_secondarypanel1").text

    if text == "Secondary Host/IP":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Port*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='portpanel1']").text

    if text == "Port*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of SMS Cost*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='costpanel1']").text

    if text == "SMS Cost*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of TPS*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='tpspanel1']").text

    if text == "TPS*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of no of binds')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("num_bindspanel1").text

    if text == "No. of Binds*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Smppc auto bind')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("auto_bindpanel1").text

    if text == "Auto Bind*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Supports Flash*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='supports_flashpanel1']").text

    if text == "Supports Flash*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of SMPP Bind Type*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='modepanel1']").text

    if text == "SMPP Bind Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of SMPPC Remarks')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='remarkspanel1']").text

    if text == "Remarks":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of SMPPC Create')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("save_smppc").get_attribute("value")

    if text == "Create":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'check text of sms charge type')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_id("sms_chargespanel1").text
#
#     if text == "SMS Charges Type*":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

# @then(u'check text of dlt charge type')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_id("dlt_chargespanel1").text
#
#     if text == "DLT Charges Type*":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'click on cancel of add smppc')
def step_impl(context):
    text = context.driver.find_element_by_id("cancel").get_attribute("value")
    if text == "Cancel":
        time.sleep(1)
        button = context.driver.find_element_by_xpath("//*[@id='cancel']")
        context.driver.execute_script("arguments[0].click();", button)
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()