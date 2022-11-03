import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'click on new sms button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("new_sms")
    context.driver.execute_script("arguments[0].click();", button)


# @then(u'click on Campaign SMS')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_xpath("//*[@id='campaign_sms_page_link']/img")
#     context.driver.execute_script("arguments[0].click();", button)


@then(u'check if New SMS/Campaign SMS text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='dashboard']/div[1]/p[1]").text

    if text == "New SMS/Campaign SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check campaign sms tab text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("pills-campaign-tab").text

    if text == "Campaign SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on the choose file in Campaign SMS tab')
def step_impl(context):
    time.sleep(1)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/fileFormats/csv_files/10.csv")
    time.sleep(1)
    context.driver.switch_to.default_content()


@then(u'check if Campaign Name text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[1]/div[1]/label").text
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[1]/div[1]/label").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[1]/div[1]/label").text

    # // *[ @ id = "dashboard"] / div[2] / div[1] / div[2] / div[1] / div[1] / label
    # Xpath change issue (of Campaign Name)
    if text == "Campaign Name *":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Sender ID text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[1]/div[2]/label").text
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[1]/div[2]/label").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[1]/div[2]/label").text

    if text == "Sender ID*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on sender id search box and select the first option')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('sender_id'))
    select.select_by_value('123456')


@then(u'check if Select Group/s text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/label").text

    if text == "Select Group/s":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Remove Duplicate Numbers text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[3]/div[1]/label[2]").text
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/div[1]/label[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div[1]/label[2]").text

    if text == "Remove Duplicate Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Remove Invalid Numbers text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[3]/div[2]/label[2]").text
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/div[2]/label[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div[2]/label[2]").text

    if text == "Remove Invalid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Content text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[4]/div[1]/label[3]").text
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[4]/div[1]/label[3]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[4]/div[1]/label[3]").text

    if text == "Content*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on insert template button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("insert_template")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check if Insert Template text  is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[1]/h6").text

    if text == "Insert Template":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Select Template Type text  is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/p[1]").text

    if text == "Select Template Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Select Template text  is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/p[2]").text

    if text == "Select Template":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Template ID text  is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/label").text

    if text == "Template ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Parameter text  is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='parameter']/div[1]/span").text

    if text == "Parameter":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Template content text  is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='parameter']/div[2]/label").text

    if text == "Template content":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on cancel button inside insert template button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("cancel_modal")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check if clear text second is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='Clear']").text

    if text == "clear":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Save as Template text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[4]/div[2]/div/p").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[4]/div[2]/div/p").text

    if text == "Save as Template":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Allow Multi Part SMS text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[5]/div[1]/label[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[5]/div[1]/label[2]").text

    if text == "Allow Multi Part SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select the Allow Multi Part SMS checkbox in campaign sms')
def step_impl(context):
    time.sleep(1)
    # button = context.driver.find_element_by_xpath(
    #     "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[5]/div[1]/label[1]/input")
    button = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[5]/div[1]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Allow Unicode text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[5]/div[2]/label[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[5]/div[2]/label[2]").text

    if text == "Allow Unicode":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Send as Flash SMS text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[5]/div[3]/label[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[5]/div[3]/label[2]").text

    if text == "Send as Flash SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Schedule SMS text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[6]/div/label[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[6]/div/label[2]").text

    if text == "Schedule SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if cancel text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='cancel']").get_attribute('value')

    if text == "Cancel":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Save as Draft text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='save_as_draft']").get_attribute('value')

    if text == "Save as Draft":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if send text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='send']").get_attribute('value')

    if text == "Send":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Invalid Numbers text inside send button is present or not in campaign sms')
def step_impl(context):
    time.sleep(2)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/label").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[2]/div[2]/div[3]/label").text

    if text == "Invalid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Duplicate Numbers text inside send button is present or not')
def step_impl(context):
    time.sleep(2)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[4]/label").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[4]/label").text

    if text == "Duplicate Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the DND Numbers text inside send button of campaign is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[5]/label").text

    if text == "DND Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Blacklisted Numbers text inside send button of campaign is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[6]/label").text

    if text == "Blacklisted Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the Valid Numbers inside send button is present or not in campaign sms')
def step_impl(context):
    time.sleep(2)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[5]/label").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[7]/label").text

    if text == "Valid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the SMS Character Count text inside send button is present or not in campaign sms')
def step_impl(context):
    time.sleep(2)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[6]/label").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[8]/label").text

    if text == "SMS Character Count":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Total Required SMS Credits text inside sender button is present or not in campaign sms')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[7]/label").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[9]/label").text

    if text == "Total Required SMS Credits":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Schedule Time text inside send button is present or not in campaign sms')
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

# @then(u'Total Balance Required text inside send button is present or not in campaign sms')
# def step_impl(context):
#     time.sleep(1)
#     # text = context.driver.find_element_by_xpath(
#     #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[2]/div[10]/label").text
#     text = context.driver.find_element_by_xpath(
#         "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/div[10]/label").text
#
#     if text == "Total Balance Required":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"


@then(u'check if Sender ID text is present inside view schedule tab or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div/table/tbody/tr/th[1]").text

    if text == "Sender ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Scheduled Date Time text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[2]").text

    if text == "Scheduled Date Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Message text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[3]").text

    if text == "Message":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Valid Numbers text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[4]").text

    if text == "Valid Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


# @then(u'check if Template Length text is present or not')
@then(u'check if Message Length text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[5]").text

    # if text == "Template Length":
    if text == "Message Length":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Total Credits text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[6]").text

    if text == "Total Credits":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Status text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[7]").text

    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Action text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div/table/tbody/tr/th[8]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()