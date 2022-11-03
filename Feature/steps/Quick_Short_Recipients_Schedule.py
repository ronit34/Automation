from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
import datetime
current_time = datetime.datetime.now()
from pytz import timezone
from datetime import datetime, date
now = datetime.now()

@then(u'Schedule sms')
def schedule(context):
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
    select = Select(context.driver.find_element(By.XPATH, "//*[@id='dashboard']/div[2]/div[1]/div/div[7]/div[2]/div[1]/select"))
    select.select_by_value(hours)
    time.sleep(1)
    select = Select(
        context.driver.find_element(By.XPATH, "//*[@id='dashboard']/div[2]/div[1]/div/div[7]/div[2]/div[2]/select"))
    select.select_by_value(minutes)


@then(u'check change in credits after schedule "{verify}"')
def step_impl(context,verify):
    time.sleep(3)
    creds = context.driver.find_element(By.XPATH, "//*[@id='available_credits']").text
    credits = int(creds.replace(',', ''))

    time.sleep(2)
    context.driver.find_element(By.ID, "confirm_send_sms").click()

    time.sleep(1)
    context.driver.refresh()

    time.sleep(2)
    creds_new = context.driver.find_element(By.XPATH, "//*[@id='available_credits']").text
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

@then(u'click on View Schedule')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "pills-campaign-summary-tab")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(4)

@then(u'check the scheduled sms is present')
def step_impl(context):
    schedule = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div/table/tbody/tr[2]/td[1]").text
    if schedule == '123456':
        assert True, f"Scheduled sms is present"
    else:
        assert False, f"Scheduled sms is not present"

    # time.sleep(1)
    # context.driver.close()