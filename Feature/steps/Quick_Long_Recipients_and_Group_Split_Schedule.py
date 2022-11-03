from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pytz import timezone
import datetime

from selenium.webdriver.support.select import Select

current_time = datetime.datetime.now()

from datetime import datetime,date
now = datetime.now()

@then(u'select group')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "groupDropdown")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("501")


@then(u'insert data')
def step_impl(context):
    # click on Insert Template template_name
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("serv_imp")

    # select template as English Long
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("1301")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on schedule sms')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.NAME, "schedule_check")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on split schedule')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.NAME, "split_check")
    context.driver.execute_script("arguments[0].click();", button)

    curr = datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")
    print(curr)
    hours = curr[0:2]
    minutes = curr[3:5]
    print("Current Hour is:" + hours)
    print("Current Minute is:" + minutes)
    min = int(minutes)
    min = min + 17
    print(min)
    if min >= 60:
        val = min - 60
        if hours == "23":
            hours = str(00)
            print("Hour is:" + hours)
        else:
            hour = int(hours) + 1
            if hour < 10:
                hours = '0' + str(hour)
                print("Hour is:" + hours)
            else:
                hours = str(hour)
                print("Hour is:" + hours)
        if val <= 9:
            minutes = '0' + str(val)
            print("Minutes is:" + minutes)

        else:
            minutes = str(val)
            print("Minutes is:" + minutes)
    else:
        minutes = str(min)
        print(hours)
        print("Minutes is:" + minutes)
    time.sleep(1)
    select = Select(
        context.driver.find_element_by_xpath(
            "//*[@id='dashboard']/div[2]/div[1]/div/div[7]/div[2]/div[1]/div[2]/div[1]/select"))
    select.select_by_value(hours)
    time.sleep(1)
    select = Select(
        context.driver.find_element_by_xpath(
            "//*[@id='dashboard']/div[2]/div[1]/div/div[7]/div[2]/div[1]/div[2]/div[2]/select"))
    select.select_by_value(minutes)
    context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[7]/div[2]/div[2]/input").send_keys("12")

    button = context.driver.find_element(By.ID, "split_more")
    context.driver.execute_script("arguments[0].click();", button)


    curr = datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")
    print(curr)
    hours = curr[0:2]
    minutes = curr[3:5]
    print("Current Hour is:" + hours)
    print("Current Minute is:" + minutes)
    min = int(minutes)
    min = min + 17
    print(min)
    if min >= 60:
        val = min - 60
        if hours == "23":
            hours = str(00)
            print("Hour is:" + hours)
        else:
            hour = int(hours) + 1
            if hour < 10:
                hours = '0' + str(hour)
                print("Hour is:" + hours)
            else:
                hours = str(hour)
                print("Hour is:" + hours)
        if val <= 9:
            minutes = '0' + str(val)
            print("Minutes is:" + minutes)

        else:
            minutes = str(val)
            print("Minutes is:" + minutes)
    else:
        minutes = str(min)
        print(hours)
        print("Minutes is:" + minutes)
    time.sleep(1)
    select = Select(
        context.driver.find_element_by_xpath(
            "//*[@id='dashboard']/div[2]/div[1]/div/div[7]/div[3]/div[1]/div[2]/div[1]/select"))
    select.select_by_value(hours)
    time.sleep(1)
    select = Select(
        context.driver.find_element_by_xpath(
            "//*[@id='dashboard']/div[2]/div[1]/div/div[7]/div[3]/div[1]/div[2]/div[2]/select"))
    select.select_by_value(minutes)
    context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[7]/div[3]/div[2]/input").send_keys("11")

@then(u'click on send')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)

    # click on multipart SMS
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='bd-example-modal-lg']/div/div/div[2]/p").text
    time.sleep(2)
    if text == "Message too long, Select Multipart !!!":
        time.sleep(2)
        button = context.driver.find_element(By.ID, "ok_modal")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        button = context.driver.find_element(By.NAME, "multipart_check")
        context.driver.execute_script("arguments[0].click();", button)

        time.sleep(1)
        button = context.driver.find_element(By.ID, "send")
        context.driver.execute_script("arguments[0].click();", button)
    else:
        time.sleep(1)
        button = context.driver.find_element(By.ID, "send")
        context.driver.execute_script("arguments[0].click();", button)

@then(u'check change in credits after splitting long sms "{verify}"')
def step_impl(context, verify):
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

    time.sleep(3)
    creds = context.driver.find_element_by_xpath("//*[@id='available_credits']").text
    credits = int(creds.replace(',', ''))

    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='bd-example-modal-lg']/div/div/div[2]/p").text
    time.sleep(1)
    if text == "Do you really want to split this campaign ?":
        time.sleep(2)
        button = context.driver.find_element(By.ID, "proceed")
        context.driver.execute_script("arguments[0].click();", button)

        time.sleep(2)
        button = context.driver.find_element(By.ID, "confirm_send_sms")
        context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    context.driver.refresh()
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

    # time.sleep(1)
    # context.driver.close()





