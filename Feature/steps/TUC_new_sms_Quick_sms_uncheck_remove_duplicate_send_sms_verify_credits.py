import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Quick English SMS')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         "//*[@id='quick_sms_page_link']/div/img[2]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Recipient')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "recipient_numbers").send_keys("543261236\n7008427274\n9542886182\n8605493727"
                                                                      "\n6301459238\n7008427274\n72543254262541")


@then(u'Uncheck Remove Duplicate Numbers in quick sms')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/div[1]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Available credits')
def step_impl(context):
    time.sleep(3)
    creds = context.driver.find_element(By.ID, "available_credits").text
    context.credits = int(creds.replace(',', ''))
    print(context.credits, "credits")


@then(u'Verify credits according to all number wise deduct or not in quick english sms')
def step_impl(context):
    time.sleep(2)
    deduct = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/div[9]/div/p").text
    deduct_creds = int(deduct)
    print(deduct)

    time.sleep(2)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    button = context.driver.find_element(By.ID, "close_modal")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    creds_new = context.driver.find_element(By.ID, "available_credits").text
    updated_creds = int(creds_new.replace(',', ''))
    verify_creds = int(deduct_creds)
    check = context.credits - updated_creds

    print(f"Credit before sending sms ---> {context.credits}")
    print(f"Credit after sending sms ---> {updated_creds}")
    print(f"Difference in Credits ---> {check}")

    if check == verify_creds:
        print(f"{check} ---> Credit deduction is correct")
        print(f"{check} ---> Credit deduction is correct")
    else:
        assert False, print(f"{check} ---> Credit deduction is wrong")

