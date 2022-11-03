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

@then(u'click on split schedule sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.NAME, "split_check")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'enter number of splits')
def step_impl(context):
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
            "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[8]/div[2]/div[1]/div[2]/div[1]/select"))
    select.select_by_value(hours)
    time.sleep(1)
    select = Select(
        context.driver.find_element_by_xpath(
            "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[8]/div[2]/div[1]/div[2]/div[2]/select"))
    select.select_by_value(minutes)
    context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[8]/div[2]/div[2]/input").send_keys("5")

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
            "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div[1]/select"))
    select.select_by_value(hours)
    time.sleep(1)
    select = Select(
        context.driver.find_element_by_xpath(
            "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div[2]/select"))
    select.select_by_value(minutes)
    context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[8]/div[3]/div[2]/input").send_keys("5")


@then(u'click on send of dynamic')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(2)
    # button = context.driver.find_element(By.ID, "proceed")
    # context.driver.execute_script("arguments[0].click();", button)
    #
    # time.sleep(2)
    # button = context.driver.find_element(By.ID, "confirm_send_sms")
    # context.driver.execute_script("arguments[0].click();", button)