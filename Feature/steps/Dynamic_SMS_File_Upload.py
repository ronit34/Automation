from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

@then(u'Choose unicode check File')
def step_impl(context):
    time.sleep(1)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/unicode-check.xlsx")
    context.driver.switch_to.default_content()

@then(u'Select Recipient Column')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "recipient_column")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("mobile_phone")

@then(u'Insert Data for Dynamic SMS')
def step_impl(context):
    # # select columns
    # button = context.driver.find_element(By.XPATH, "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[1]/ul/li[1]")
    # context.driver.execute_script("arguments[0].click();", button)

    # click on arrow
    button = context.driver.find_element(By.XPATH, "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/button[3]")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("serv_imp")

    # select template as one variable
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("Long Three Var")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click on preview')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/input")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on send button of dynamic')
def step_impl(context):
    # Select Multipart
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[6]/div[1]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Allow unicode
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[6]/div[2]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)

    # Click on Send
    time.sleep(1)
    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check change in credits after the sms is sent "{verify}"')
def step_impl(context,verify):
    time.sleep(3)
    creds = context.driver.find_element_by_xpath("//*[@id='available_credits']").text
    credits = int(creds.replace(',', ''))

    time.sleep(2)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    creds_new = context.driver.find_element_by_xpath("//*[@id='available_credits']").text
    updated_creds = int(creds_new.replace(',', ''))
    verify_creds = int(verify)
    check = credits - updated_creds

    print(f"Credit before sending sms ---> {credits}")
    print(f"Credit after sending sms ---> {updated_creds}")
    print(f"Difference in Credits ---> {check}")

    if (check == verify_creds):
        print(f"{check} ---> Credit deduction is correct")
        print(f"{check} ---> Credit deduction is correct")
    else:
        assert False, print(f"{check} ---> Credit deduction is wrong")


