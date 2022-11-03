import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# @then(u'click on Dynamic SMS')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_xpath("//*[@id='dynamic_sms_page_link']/img")
#     context.driver.execute_script("arguments[0].click();", button)

@then(u'check if New SMS/Dynamic SMS text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='dashboard']/div[1]/p[1]").text

    if text == "New SMS/Dynamic SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Dynamic SMS tab text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("pills-campaign-tab").text

    if text == "Dynamic SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on the choose file in Dynamic SMS tab')
def step_impl(context):
    time.sleep(1)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/6var.xlsx")
    time.sleep(1)
    context.driver.switch_to.default_content()
#
# @then(u'check if Campaign Name text is present or not')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_xpath(
#         "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[1]/div[1]/label").text
#
#     if text == "Campaign Name":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"
#
# @then(u'check if Sender ID text is present or not')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_xpath(
#         "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[1]/div[2]/label").text
#
#     if text == "Sender ID":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"
#
# @then(u'click on sender id search box and select the first option')
# def step_impl(context):
#     time.sleep(1)
#     select = Select(context.driver.find_element_by_id('sender_id'))
#     select.select_by_value('qwerty')

@then(u'check if select recipient column text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #         "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div/label").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[2]/div/label").text

    if text == "Select Recipient Column *":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Available columns text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/div/div/div[1]/div").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[1]/div").text

    if text == "Available Columns":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Selected columns text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/div/div/div[3]/div").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[3]/div").text

    if text == "Selected Columns":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select from available columns for selected columns')
def step_impl(context):
    #clicking on arrow button
    button = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/button[3]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if show preview text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/input").get_attribute("value")
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/input").get_attribute("value")

    if text == "Show Preview":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on show preview')
def step_impl(context):
    # button = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/input")
    button = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/input")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if preview text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[1]/p[1]").text

    if text == "Preview":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if mobile text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/table/tbody/tr[1]/th[1]").text

    if text == "Mobile":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if message text is present or not in preview')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/table/tbody/tr[1]/th[2]").text

    if text == "Message":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if ok text of dynamic text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='ok_modal']").get_attribute("value")

    if text == "OK":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on ok button of preview')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='ok_modal']")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Remove Duplicate Numbers text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[2]/div[1]/label[2]").text

    if text == "Remove Duplicate Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Remove Invalid Numbers text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[2]/div[2]/label[2]").text
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[4]/div/label[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[4]/div/label[2]").text

    if text == "Remove Invalid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Content text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[3]/div[1]/label[3]").text
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[5]/div[1]/label[3]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[5]/div[1]/label[3]").text

    if text == "Content*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on insert template button in dynamic sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("insert_template")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Insert Template text  is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[1]/h6").text

    if text == "Insert Template":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Select Template Type text  is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/p[1]").text

    if text == "Select Template Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Select Template text  is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/p[2]").text

    if text == "Select Template*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select dynamic template from Select Template dropdown')
def step_impl(context):
    time.sleep(1)
    temp = context.driver.find_element(By.ID, "template_name")
    select = Select(temp)
    select.select_by_visible_text("Three Variable")


@then(u'check if Template ID text  is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/label").text

    if text == "Template ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Parameter text  is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='parameter']/div[1]/span").text

    if text == "Parameter":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Template content text  is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='parameter']/div[2]/label").text

    if text == "Template content":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if clear text second is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='Clear']").text

    if text == "clear":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'check if Save as Template text is present or not in dynamic sms')
# def step_impl(context):
#     time.sleep(1)
#     # text = context.driver.find_element_by_xpath(
#     #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[5]/div[2]/div/p").text
#     text = context.driver.find_element_by_xpath(
#         "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[5]/div[2]/div/p").text
#
#     if text == "Save as Template":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'check if Allow Multi Part SMS text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[6]/div[1]/label[2]").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[6]/div[1]/label[2]").text

    if text == "Allow Multi Part SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select the Allow Multi Part SMS checkbox in dynamic sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[6]/div[1]/label[2]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Allow Unicode text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[6]/div[2]/label[2]").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[6]/div[2]/label[2]").text

    if text == "Allow Unicode":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Send as Flash SMS text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[6]/div[3]/label[2]").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[6]/div[3]/label[2]").text

    if text == "Send as Flash SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Schedule SMS text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[7]/div/label[2]").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[7]/div/label[2]").text

    if text == "Schedule SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Scrub DND text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[7]/div[2]/label[2]").text

    if text == "Scrub DND":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if cancel text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='cancel']").get_attribute('value')

    if text == "Cancel":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of Save as Draft button text in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("save_as_draft").get_attribute('value')

    if text == "Save as Draft":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if send text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='send']").get_attribute('value')

    if text == "Send":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'click on send button')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_xpath("//*[@id='send']")
#     context.driver.execute_script("arguments[0].click();", button)

@then(u'check the SMS Confirmation text inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[1]/h6").text
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[1]/h6").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[1]/h6").text

    if text == "SMS Confirmation":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Sender ID text inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[1]/label[1]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[2]/div[1]/label[1]").text

    if text == "Sender ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Message text inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[1]/label[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[2]/div[1]/label[2]").text

    if text == "Message":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the SMS Character Count inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[2]/div[2]/div[3]/label").text

    if text == "SMS Character Count":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Valid Numbers inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[4]/label").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[4]/label").text

    if text == "Valid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Invalid Numbers text inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[5]/label").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[5]/label").text

    if text == "Invalid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the DND Numbers text inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[6]/label").text

    if text == "DND Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Invalid Records text inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[6]/label").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[7]/label").text

    if text == "Invalid Records":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Blacklisted Numbers text inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[8]/label").text

    if text == "Blacklisted Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Total Records text inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[7]/label").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[9]/label").text

    if text == "Total Records":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Total Required SMS Credits text inside sender button is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[8]/label").text
    # text = context.driver.find_element_by_xpath(
    #     "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[8]/label").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[2]/div[2]/div[10]/label").text

    if text == "Total Required SMS Credits":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Schedule Time text inside send button is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[9]/label").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[11]/label").text

    if text == "Schedule Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'Total Balance Required text inside send button is present or not')
# def step_impl(context):
#     time.sleep(2)
#     # text = context.driver.find_element_by_xpath(
#     #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[11]/label").text
#     text = context.driver.find_element_by_xpath(
#         "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[11]/label").text
#
#     if text == "Total Balance Required":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'click on cancel button inside send button in dynamic sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("cancel")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on view schedule tab in dynamic sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='pills-campaign-summary-tab']")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Sender ID text is present inside view schedule tab or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[1]").text

    if text == "Sender ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Scheduled Date Time text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[2]").text

    if text == "Scheduled Date Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Message text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[3]").text

    if text == "Message":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Valid Numbers text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[4]").text

    if text == "Valid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Status text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[5]").text

    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action text is present or not in dynamic sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[6]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()