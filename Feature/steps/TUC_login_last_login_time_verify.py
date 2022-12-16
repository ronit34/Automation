import time
import datetime
from behave import *
from selenium.webdriver.common.by import By


@then(u'Stored time now')
def step_impl(context):
    # time.sleep(4)
    last_logi_time = datetime.datetime.now()
    # context.login_time = last_logi_time.strftime("%Y-%m-%d %H:%M:%S")
    year = int(last_logi_time.strftime("%Y"))
    month = int(last_logi_time.strftime("%m"))
    day = int(last_logi_time.strftime("%d"))
    hour = int(last_logi_time.strftime("%H"))
    minute = int(last_logi_time.strftime("%M"))
    second = int(last_logi_time.strftime("%S"))
    context.login_time = str(year) + "-" + str(month) + "-" + str(day) \
                         + " " + str(hour) + ":" + str(minute) + ":" + str(second)
    print(year, month, day, hour, minute, second)


@then(u'Click on profile Login History')
def step_impl(context):
    time.sleep(2)
    profile_button = context.driver.find_element(By.XPATH, "//*[@id='profile']/div/p[1]")
    context.driver.execute_script("arguments[0].click();", profile_button)
    time.sleep(1)
    login_history_button = context.driver.find_element(By.XPATH, "//*[@id='profiledropdown']/li[4]/a")
    context.driver.execute_script("arguments[0].click();", login_history_button)


@then(u'Verify last login time')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='campaign-table']/tbody/tr[2]/td[2]").text
    print("=====: ", txt)
    last_login_tim_history = context.login_time
    print("++++==: ", last_login_tim_history)
    if txt == last_login_tim_history:
        assert True
    else:
        assert False
