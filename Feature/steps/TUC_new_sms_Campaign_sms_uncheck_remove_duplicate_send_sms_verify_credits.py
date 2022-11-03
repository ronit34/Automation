import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on choose file in campaign sms')
def step_impl(context):
    context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys("/home/ronit/Desktop/sms service/campaign.csv")


@then(u'Uncheck Remove Duplicate Numbers')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[3]/div[1]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify credits according to all number wise deduct or not')
def step_impl(context):
    time.sleep(3)
    creds = context.driver.find_element(By.ID, "available_credits").text
    credits = int(creds.replace(',', ''))
    print(credits, "credits")

    time.sleep(2)
    deduct = context.driver.find_element(By.XPATH, "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[2]/div[2]/div[9]/div/p").text
    deduct_creds = int(deduct)
    print(deduct)

    time.sleep(2)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    creds_new = context.driver.find_element(By.ID, "available_credits").text
    updated_creds = int(creds_new.replace(',', ''))
    verify_creds = int(deduct_creds)
    check = credits - updated_creds

    print(f"Credit before sending sms ---> {credits}")
    print(f"Credit after sending sms ---> {updated_creds}")
    print(f"Difference in Credits ---> {check}")

    if check == verify_creds:
        print(f"{check} ---> Credit deduction is correct")
        print(f"{check} ---> Credit deduction is correct")
    else:
        assert False, print(f"{check} ---> Credit deduction is wrong")
