from behave import *
from selenium.webdriver.common.by import By
import time
@then(u'check text of Gateway Name')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[1]/a").text

    if text == "Gateway Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Gateway Description')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[2]/a").text

    if text == "Description":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Gateway Carrier Name')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[3]").text

    if text == "Carrier Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Gateway Circle Name')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[4]/a").text

    if text == "Circle Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Gateway Action')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[5]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Gateway +Add Gateway')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[2]/a").text
    text = context.driver.find_element_by_id("create_gateway").text

    # if text == "+Add Gateway":
    if text == "+ Add Gateway":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


# @then(u'click on SMPPC')
# def step_impl(context):
#     time.sleep(2)
#     context.driver.find_element_by_xpath("//*[@id='smppc_view']").click()


@then(u'check text of SMPPC')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='smppc_view']").text

    if text == "SMPPC":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of SMPPC Name/Carrier/Vendor/AccountType/Circle')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[3]/table/tbody/tr[1]/th[1]").text

    if text == "Name/Carrier/Vendor/AccountType/Circle":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of SMPPC Gateway id')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[3]/table/tbody/tr[1]/th[2]").text
    if text == "Gateway Id":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"



@then(u'check text of SMPPC TPS')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(" //*[@id='pills-campaign']/div[3]/table/tbody/tr[1]/th[3]").text

    if text == "TPS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"




@then(u'check text of SMPPC Binds')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[4]").text

    if text == "Binds":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of SMPPC Action')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[5]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of SMPPC +Add SMPPC')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='create_smppc']").text

    if text == "+Add SMPPC":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on Routing')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "routing_view")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check text of Routing')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='routing_view']").text

    if text == "Routing":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of +Add Routing')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='create_routing']").text

    # if text == "+Add Routing":
    if text == "+ Add Routing":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on  Default Gateway')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='default_gateway']").click()

@then(u'check text of Default Gateway')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='default_gateway']").text

    if text == "Default Gateway":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Default Gateway OTP*')
def step_impl(context):
    time.sleep(4)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/label").text

    if text == "OTP*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Default Gateway Service Implicit*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/div[2]/label").text

    if text == "Service Implicit*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Default Gateway Service Explicit*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/div[3]/label").text

    if text == "Service Explicit*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Default Gateway Promotional*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/div[4]/label").text

    if text == "Promotional*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Default Gateway TransPromo*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/div[5]/label").text

    if text == "TransPromo*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Default Gateway Government Exempted*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/div[6]/label").text
    if text == "Government Exempted*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Default Gateway Simroute*')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/div[7]/label").text

    if text == "Simroute*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Default Gateway Save Default Gateways')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("save_default_gateways").get_attribute("value")

    if text == "Save Default Gateways":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()