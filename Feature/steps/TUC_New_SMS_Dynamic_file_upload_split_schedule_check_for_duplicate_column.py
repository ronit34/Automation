import time
from datetime import datetime, timedelta
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Choose file for dynamic')
def step_impl(context):
    time.sleep(2)
    context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys("/home/ronit/Desktop/sms service/dublicate dynamic .csv")


@then(u'Select Columns')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[1]/ul/li[1]")
    context.driver.execute_script("arguments[0].click();", button)
    button1 = context.driver.find_element(By.XPATH,
                                          "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/button[1]")
    context.driver.execute_script("arguments[0].click();", button1)


@then(u'Insert Template in Dynamic')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "template_type_id"))
    select.select_by_visible_text('Promo (2)')
    time.sleep(1)
    select1 = Select(context.driver.find_element(By.ID, "template_name"))
    select1.select_by_visible_text('English Promo')
    time.sleep(1)
    button1 = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button1)


@then(u'Click on Split into multiple Campaigns')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[7]/div[2]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Split SMS and count')
def step_impl(context):
    for a in range(3):
        button = context.driver.find_element(By.XPATH, "//*[@id='split_more']/p[1]")
        context.driver.execute_script("arguments[0].click();", button)
        a += 1

    for b in range(0, 4):
        context.driver.find_element(By.XPATH, f"//*[@id='dashboard']/div[2]/div[1]/div[3]/div[8]/div[{2+b}]/div[2]/input").send_keys('2')
        b += 1

    time.sleep(1)
    for c in range(0, 4):
        fill_time = (datetime.now() + timedelta(minutes=18))
        select = Select(context.driver.find_element(By.XPATH, f"//*[@id='dashboard']/div[2]/div[1]/div[3]/div[8]/div[{2+c}]/div[1]/div[2]/div[1]/select"))
        select.select_by_visible_text((fill_time + timedelta(minutes=c)).strftime("%H"))

        select = Select(context.driver.find_element(By.XPATH, f"//*[@id='dashboard']/div[2]/div[1]/div[3]/div[8]/div[{2+c}]/div[1]/div[2]/div[2]/select"))
        select.select_by_visible_text((fill_time + timedelta(minutes=c)).strftime("%M"))

        c += 1
        time.sleep(2)


@then(u'Click on send In dynamic sms')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on yes button of pop-up')
def step_impl(context):
    time.sleep(10)
    button = context.driver.find_element(By.ID, "proceed")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify duplicate number')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='dashboard']/div[2]/div[1]/div[3]/table/tbody/tr[6]/th[3]")
    print(txt)
    if txt:
        assert True
    else:
        assert False


@then(u'Click on proceed')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)