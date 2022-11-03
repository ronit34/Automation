import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Tenants')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "tenant_view")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub_heading and placeholder create_tenant')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.ID, "current_date").text

    if txt == "Tuesday 11 October 2022":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    tenant_name = context.driver.find_element(By.ID, "name").get_attribute('placeholder')
    print(tenant_name)
    if tenant_name == "Enter Tenant Name":
        assert True, f"{tenant_name}"
    else:
        assert False, f"{tenant_name}"

    desc = context.driver.find_element(By.ID, "description").get_attribute('placeholder')
    print(desc)
    if desc == "Enter Description":
        assert True, f"{desc}"
    else:
        assert False, f"{desc}"

    child_tuc = context.driver.find_element(By.ID, "childtuc").get_attribute('placeholder')
    print(child_tuc)
    if child_tuc == "Enter Child TUC":
        assert True, f"{child_tuc}"
    else:
        assert False, f"{child_tuc}"

    smpps = context.driver.find_element(By.ID, "smpps").get_attribute('placeholder')
    print(smpps)
    if smpps == "Enter SMPPS":
        assert True, f"{smpps}"
    else:
        assert False, f"{smpps}"

    sms_api = context.driver.find_element(By.ID, "smsapi").get_attribute('placeholder')
    print(sms_api)
    if sms_api == "Enter SMS API":
        assert True, f"{sms_api}"
    else:
        assert False, f"{sms_api}"
