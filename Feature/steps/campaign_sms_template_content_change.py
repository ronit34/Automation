from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


import CommonUtility as CU
new_campaign_sms_inputObj = CU.new_campaign_sms_input()


@then(u'sent sms through campaign')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.NAME, "file1").send_keys(
        "/home/onexadmin/Downloads/fileFormats/csv_files/10.csv")

    time.sleep(1)
    context.driver.switch_to.default_content()

    time.sleep(1)
    for element_id in new_campaign_sms_inputObj.new_campaign_sms_input_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_campaign_sms_inputObj.new_campaign_sms_input_list[element_id])
        print(f"{element_id}")

    # click on Insert Template template_name
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("serv_imp")

    # select template as English short
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("English Short")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(4)
    button = context.driver.find_element(By.ID, "msgText")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(3)
    button.clear()
    button.send_keys("select from dropdown")

    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)

    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[2]/div[1]/p[2]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[2]/div[1]/p[2]").text
    if text == "select from dropdown":
        context.driver.find_element_by_id("confirm_send_sms").click()
    else:
        assert False, "Message does not match"

    # time.sleep(2)
    # context.driver.find_element_by_xpath("//*[@id='dashboard']/div[2]/div[1]/div/div[2]/div[2]/div/a").click()
    #
    # time.sleep(2)
    # context.driver.find_element_by_xpath("//*[@id='dashboard']/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td/a/img").click()
    # time.sleep(2)
    # text = context.driver.find_element_by_xpath("//*[@id='bd-example-modal-lg']/div/div/div[2]/p").text
    # if text == "select from dropdown":
    #     context.driver.find_element_by_id("ok_modal").click()
    # else:
    #     assert False, "Message does not match"

@then(u'click on reports')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='menu_report']/p").click()


@then(u'click on Campaigns')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "pills-campaign-tab")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element_by_id("search").click()

    time.sleep(1)
    # context.driver.find_element_by_xpath("//*[@id='campaign-summary-table']/tbody/tr[2]/td[11]/a/img").click()
    context.driver.find_element_by_xpath(
        "//*[@id='campaign-summary-table']/tbody/tr[2]/td[10]/a/img").click()

    time.sleep(1)
    text = context.driver.find_element_by_xpath(
            "//*[@id='bd-example-modal-lg']/div/div/div[2]/p").text


    if text == "select from dropdown":
        context.driver.find_element_by_id("ok_modal").click()
    else:
        assert False, "Message does not match"

@then(u'click on download')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "dropdownMenuLink")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    button = context.driver.find_element(By.ID, "download_csv")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "okay")
    context.driver.execute_script("arguments[0].click();", button)


    # time.sleep(1)
    # context.driver.close()









