import time
from behave import *
from selenium.webdriver.common.by import By

@then(u'click on the smpp tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='menu_smpps_view']/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if SMPP header text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "SMPP":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if the text of SMPP is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[1]/a").text

    if text == "SMPP":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if the text of SMPP ID text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[1]").text

    if text == "SMPP ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if System ID/User ID text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[2]/a").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[2]").text

    if text == "System ID/User ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Account Type text is present or not in smpp tab')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[3]/a").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[3]").text

    if text == "Account Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if SMPP Bind Type text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr/th[4]/a").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[4]").text

    if text == "SMPP Bind Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if IP Address text is present or not in smpp tab')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[5]/a").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[5]").text

    if text == "IP Address":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action text is present or not in smpp tab')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[6]").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[6]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on add smpp button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("create_smpps")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Create SMPP text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "Create SMPP":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if SMPP Account text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[1]/h5").text

    if text == "SMPP Account":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if System ID/User ID* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='systemidpanel1']").text

    if text == "System ID/User ID*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Password* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='passwordpanel1']").text

    if text == "Password*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if System Type* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='systemtypepanel1']").text

    if text == "System Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Account Type* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='accounttypepanel1']").text

    if text == "Account Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Limit SMS / Day* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='limitdaypanel1']").text

    if text == "Limit SMS / Day*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Limit SMS / Hour* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='limithourpanel1']").text

    if text == "Limit SMS / Hour*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Validity* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='validitypanel1']").text

    if text == "Validity*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if SMPP Bind Type* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='modepanel1']").text

    if text == "SMPP Bind Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if IP Address text inside add smpp is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='client_ippanel1']").text

    if text == "IP Address":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if TLV Template ID text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='templateIdpanel1']").text

    if text == "TLV Template ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if TLV Entity ID text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='entityIdpanel1']").text

    if text == "TLV Entity ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Total TPS* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='total_tpspanel1']").text

    if text == "Total TPS*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Keep Alive* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='keep_alivepanel1']").text

    if text == "Keep Alive*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Max Binds* text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='max_bindspanel1']").text

    if text == "Max Binds*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Other text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='otherpanel1']").text

    if text == "Other":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if DND_filter text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/div[1]/div[20]/div/div/div[1]/label").text

    if text == "DND_filter":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'check if Active text is present or not')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_xpath(
#         "//*[@id='pills-campaign']/div[2]/div/div[1]/div[20]/div/div/div[2]/label").text
#
#     if text == "Active":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

# @then(u'check if Forced_DLR text is present or not')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_xpath(
#         "//*[@id='pills-campaign']/div[2]/div/div[1]/div[20]/div/div/div[3]/label").text
#
#     if text == "Forced_DLR":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

# @then(u'check if Credit_Rollback text is present or not')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_xpath(
#         "//*[@id='pills-campaign']/div[2]/div/div[1]/div[20]/div/div/div[4]/label").text
#
#     if text == "Credit_Rollback":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'check if Check_Time text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[20]/div/div/div[5]/label").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[20]/div/div/div[2]/label").text

    if text == "Check_Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of create button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='save_smpps']").get_attribute('value')

    if text == "Create":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of cancel button and click on it if it is present in smpp tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='cancel']").get_attribute('value')

    if text == "Cancel":
        button = context.driver.find_element_by_id("cancel")
        context.driver.execute_script("arguments[0].click();", button)
        assert True, f"{text} is present"

    else:
        assert False, f"{text} is not present"

@then(u'check the text of bind history button and click on it if it is present')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[2]/a").text

    if text == "Bind History":
        button = context.driver.find_element_by_id("bind_history")
        context.driver.execute_script("arguments[0].click();", button)
        assert True, f"{text} is present"

    else:
        assert False, f"{text} is not present"

@then(u'click on bind history tab')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element_by_id("bind_history")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if IP text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[1]").text

    if text == "IP":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Bind/Unbind text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[2]").text

    if text == "Bind/Unbind":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if DateTime text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[3]").text

    if text == "DateTime":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()