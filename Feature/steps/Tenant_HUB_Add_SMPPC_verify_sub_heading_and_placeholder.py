from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Verify Sub-heading and Placeholder_SMPPC')
def step_impl(context):
    time.sleep(2)
    sub_head_txt = context.driver.find_element(By.ID, "current_date").text
    print(sub_head_txt)
    if sub_head_txt == "Monday 10 October 2022":
        assert True, f"{sub_head_txt}"
    else:
        assert False, f"{sub_head_txt}"

    name = context.driver.find_element(By.ID, "name").get_attribute('placeholder')
    print(name)
    if name == "Name":
        assert True, f"{name}"
    else:
        assert False, f"{name}"

    smpp_loginid = context.driver.find_element(By.ID, "smpplogin").get_attribute('placeholder')
    print(smpp_loginid)
    if smpp_loginid == "Enter SMPP Login ID":
        assert True, f"{smpp_loginid}"
    else:
        assert False, f"{smpp_loginid}"

    system_id = context.driver.find_element(By.ID, "username").get_attribute('placeholder')
    print(system_id)
    if system_id == "Enter System ID":
        assert True, f"{system_id}"
    else:
        assert False, f"{system_id}"

    password = context.driver.find_element(By.ID, "password").get_attribute('placeholder')
    print(password)
    if password == "Enter Password":
        assert True, f"{password}"
    else:
        assert False, f"{password}"

    primary_host = context.driver.find_element(By.ID, "host").get_attribute('placeholder')
    print(primary_host)
    if primary_host == "Enter Primary Host/IP":
        assert True, f"{primary_host}"
    else:
        assert False, f"{primary_host}"

    secondary_host = context.driver.find_element(By.ID, "host_secondary").get_attribute('placeholder')
    print(secondary_host)
    if secondary_host == "Enter Secondary Host/IP":
        assert True, f"{secondary_host}"
    else:
        assert False, f"{secondary_host}"

    port = context.driver.find_element(By.ID, "port").get_attribute('placeholder')
    print(port)
    if port == "Enter Port":
        assert True, f"{port}"
    else:
        assert False, f"{port}"

    sms_cost = context.driver.find_element(By.ID, "cost").get_attribute('placeholder')
    print(sms_cost)
    if sms_cost == "Enter SMS Cost":
        assert True, f"{sms_cost}"
    else:
        assert False, f"{sms_cost}"

    tps = context.driver.find_element(By.ID, "tps").get_attribute('placeholder')
    print(tps)
    if tps == "Enter TPS":
        assert True, f"{tps}"
    else:
        assert False, f"{tps}"

    binds = context.driver.find_element(By.ID, "num_binds").get_attribute('placeholder')
    print(binds)
    if binds == "Enter No. of Binds":
        assert True, f"{binds}"
    else:
        assert False, f"{binds}"

    remark = context.driver.find_element(By.ID, "remarks").get_attribute('placeholder')
    print(remark)
    if remark == "Enter Remark":
        assert True, f"{remark}"
    else:
        assert False, f"{remark}"

