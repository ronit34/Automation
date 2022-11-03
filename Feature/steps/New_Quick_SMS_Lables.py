import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'click on  Quick English SMS')
def step_impl(context):
    time.sleep(1)
    # button = context.driver.find_element_by_xpath("//*[@id='quick_sms_page_link']/img")
    button = context.driver.find_element_by_xpath("//*[@id='quick_sms_page_link']/div/img[1]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if New SMS/Quick English SMS text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "New SMS/Quick English SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of Quick SMS tab')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_id("pills-campaign-tab").text

    if text == "Quick SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Campaign Name text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[1]/label").text

    if text == "Campaign Name *":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Sender ID text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[2]/label").text

    if text == "Sender ID*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on sender id search box and select the first option in quick sms')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('sender_id'))
    select.select_by_value('123456')

@then(u'check if Recipients text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/label").text

    if text == "Recipients*(New Number on New Line)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Enter valid number in Recipients text field')
def step_impl(context):
    context.driver.find_element_by_id("recipient_numbers").send_keys("8292037493")

@then(u'check if Select Group/s text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/label").text

    if text == "Select Group/s":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if clear text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='Clear']").text

    if text == "clear":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Remove Duplicate Numbers text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/div[1]/label[2]").text

    if text == "Remove Duplicate Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Remove Invalid Numbers text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/div[2]/label[2]").text

    if text == "Remove Invalid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Content text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[1]/label[3]").text

    if text == "Content*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on insert template button in quick sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("insert_template")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Insert Template text  is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[1]/h6").text

    if text == "Insert Template":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Select Template Type text  is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/p[1]").text

    if text == "Select Template Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select the template type from Select Template Type dropdown')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('template_type_id'))
    select.select_by_value('serv_imp')

@then(u'check if Select Template text  is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/p[2]").text

    if text == "Select Template*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select template from Select Template dropdown')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('template_name'))
    select.select_by_value('1301')
    # select.select_by_value('1310')

@then(u'check if Template ID text  is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/label").text

    if text == "Template ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Parameter text  is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='parameter']/div[1]/span").text

    if text == "Parameter":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Template content text  is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='parameter']/div[2]/label").text

    if text == "Template content":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on select button inside insert template button in quick sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on Insert Url text')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("insert_url")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Insert Url text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[1]/p[1]").text

    if text == "Insert URL":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if select domain text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/div[1]/label").text

    if text == "Select Domain":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'Select domain from select domain dropdown')
# def step_impl(context):
#     time.sleep(1)
#     select = Select(context.driver.find_element_by_id('template_type_id'))
#     select.select_by_value('1401')

@then(u'check if Target Url text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/div[2]/div/label").text

    if text == "Target URL":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on the Cancel Url button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/input[1]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if clear text second is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='Clear']").text

    if text == "clear":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Save as Template text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[2]/div/p").text

    if text == "Save as Template":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Allow Multi Part SMS text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[1]/label[2]").text

    if text == "Allow Multi Part SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select the Allow Multi Part SMS checkbox')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[1]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Send as Flash SMS text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[3]/label[2]").text

    if text == "Send as Flash SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Schedule SMS text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[6]/div/label[2]").text

    if text == "Schedule SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if cancel text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='cancel']").get_attribute('value')

    if text == "Cancel":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if send text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='send']").get_attribute('value')

    if text == "Send":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on the send button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("send")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check the sms confirmation text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[1]/p[1]").text

    if text == "SMS Confirmation":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check sender id text is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/label[1]").text

    if text == "Sender ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Message text is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/label[2]").text

    if text == "Message":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Invalid Numbers text is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[3]/label").text

    if text == "Invalid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Duplicate Number text is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[4]/label").text

    if text == "Duplicate Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if DND Number text is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[5]/label").text

    if text == "DND Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Blacklisted Numbers text is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[6]/label").text

    if text == "Blacklisted Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Valid Numbers text is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[7]/label").text

    if text == "Valid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if SMS Character Count is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[8]/label").text

    if text == "SMS Character Count":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"



@then(u'check if Total Required SMS Credits text is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[9]/label").text

    if text == "Total Required SMS Credits":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Schedule Time text is present or not inside send button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[10]/label").text

    if text == "Schedule Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on cancel button inside send button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("cancel_modal")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on view schedule tab in quick sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='pills-campaign-summary-tab']")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check the  text of view schedule tab in quick sms')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_id("pills-campaign-summary-tab").text

    if text == "View Schedule":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Sender ID text is present inside view schedule tab or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[1]").text

    if text == "Sender ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Scheduled Date Time text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[2]").text

    if text == "Scheduled Date Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Message text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[3]").text

    if text == "Message":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Valid Numbers text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[4]").text

    if text == "Valid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'check if Template Length text is present or not in quick sms')
@then(u'check if Message Length text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[5]").text

    # if text == "Template Length":
    if text == "Message Length":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Total Credits text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[6]").text

    if text == "Total Credits":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Status text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[7]").text

    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[8]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()