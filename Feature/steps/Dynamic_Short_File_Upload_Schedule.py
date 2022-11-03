from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
import datetime
from pytz import timezone
current_time = datetime.datetime.now()
from datetime import datetime,date
now = datetime.now()

@then(u'Choose variable File')
def step_impl(context):
    time.sleep(1)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys(
        "/home/onexadmin/Downloads/10Nos1Vars10VarLength.xlsx")
    context.driver.switch_to.default_content()


@then(u'insert values in fields')
def step_impl(context):
    # select columns
    button = context.driver.find_element(By.XPATH,
                                         "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[1]/ul/li[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # click on arrow
    button = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/button[1]")
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
    # select.select_by_value("1305")
    select.select_by_visible_text("One Variable")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Schedule dynamic sms')
def step_impl(context):
    time.sleep(3)
    schedule = context.driver.find_element(By.NAME, "schedule_check")
    context.driver.execute_script("arguments[0].click();", schedule)

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
            "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[8]/div[2]/div[1]/select"))
    select.select_by_value(hours)
    time.sleep(1)
    select = Select(
        context.driver.find_element_by_xpath(
            "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[8]/div[2]/div[2]/select"))
    select.select_by_value(minutes)


@then(u'click on send now button of dynamic sms')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

