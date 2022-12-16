import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Click on Add TUC in TA11')
def step_impl(context):
    button = context.driver.find_element(By.ID, "create_tuc")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert details in add TUC in TA11 for same name')
def step_impl(context):
    context.driver.find_element(By.ID, "name").send_keys("ICICI")
    select = Select(context.driver.find_element(By.ID, "otp_acc_type"))
    select.select_by_visible_text("On Delivery")
    select1 = Select(context.driver.find_element(By.ID, "trans_acc_type"))
    select1.select_by_visible_text("On Delivery")
    select2 = Select(context.driver.find_element(By.ID, "promo_acc_type"))
    select2.select_by_visible_text("On Delivery")
    select3 = Select(context.driver.find_element(By.ID, "gov_acc_type"))
    select3.select_by_visible_text("On Delivery")
    select4 = Select(context.driver.find_element(By.ID, "sim_acc_type"))
    select4.select_by_visible_text("On Delivery")
    select5 = Select(context.driver.find_element(By.ID, "default_acc_type"))
    select5.select_by_visible_text("On Delivery")
    select6 = Select(context.driver.find_element(By.ID, "billing_type"))
    select6.select_by_visible_text("PREPAID")
    context.driver.find_element(By.ID, "validity").send_keys("10")
    select7 = Select(context.driver.find_element(By.ID, "mask_phone"))
    select7.select_by_visible_text("Yes")

    context.driver.find_element(By.ID, "childtuc").send_keys("10")
    context.driver.find_element(By.ID, "smpps").clear()
    context.driver.find_element(By.ID, "smpps").send_keys("10")
    context.driver.find_element(By.ID, "smsapi").clear()
    context.driver.find_element(By.ID, "smsapi").send_keys("10")


@then(u'Click on create in add TUC in TA11')
def step_impl(context):
    time.sleep(2)
    if "Name*" in context.driver.page_source:
        button = context.driver.find_element(By.ID, "save_tuc")
        context.driver.execute_script("arguments[0].click();", button)
    else:
        if "Name* already exists." in context.driver.page_source:
            time.sleep(2)
            button1 = context.driver.find_element(By.ID, "cancel")
            context.driver.execute_script("arguments[0].click();", button1)
        else:
            time.sleep(2)
            button2 = context.driver.find_element(By.ID, "save_tuc")
            context.driver.execute_script("arguments[0].click();", button2)


@then(u'Verify tenant create or not in TA11')
def step_impl(context):
    time.sleep(2)
    txt = "ICICI"
    if txt in context.driver.page_source:
        assert False, f"{txt}"
    else:
        assert True, f"{txt}"
