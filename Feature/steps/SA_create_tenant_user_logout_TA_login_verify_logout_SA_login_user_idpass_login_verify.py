import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'insert detail for create tenant')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "name").send_keys("Ronit")
    context.driver.find_element(By.ID, "description").send_keys("abcd")
    context.driver.find_element(By.ID, "childtuc").send_keys(3)
    context.driver.find_element(By.ID, "smpps").send_keys(3)
    context.driver.find_element(By.ID, "smsapi").send_keys(3)


@then(u'Click on user in user_management')
def step_impl(context):
    time.sleep(3)
    button = context.driver.find_element(By.ID, "user_view")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert details in user info')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.ID, "username").send_keys("ronitqwerty")
    context.driver.find_element(By.ID, "password").send_keys("qwerty@123")
    context.driver.find_element(By.ID, "fname").send_keys("Ronit")
    context.driver.find_element(By.ID, "lname").send_keys("Patel")
    context.driver.find_element(By.ID, "email").send_keys("abc@gmail.com")
    context.driver.find_element(By.ID, "mob_no").send_keys(1234567890)
    context.driver.find_element(By.ID, "comp_name").send_keys("Onextel")
    context.driver.find_element(By.ID, "web").send_keys("https://www.onextel.com/")
    context.driver.find_element(By.ID, "other_mob_no").send_keys(9876543210)

    select = Select(context.driver.find_element(By.ID, "role_type"))
    select.select_by_visible_text('Tenant Admin')
    select1 = Select(context.driver.find_element(By.ID, "tenant"))
    select1.select_by_visible_text('Ronit(11)')


@then(u'Click on create in user info')
def step_impl(context):
    time.sleep(3)
    button = context.driver.find_element(By.ID, "save_user")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Logout from SA')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "profile")
    context.driver.execute_script("arguments[0].click();", button)
    button1 = context.driver.find_element(By.ID, "log-out")
    context.driver.execute_script("arguments[0].click();", button1)


@then(u'Verify TA login or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/p[1]").text
    print(txt)
    if txt == "Dashboard":
        assert True, "Login verify"
    else:
        assert False, "Login Failed"


@then(u'Logout from TA')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "profile")
    context.driver.execute_script("arguments[0].click();", button)
    button1 = context.driver.find_element(By.ID, "log-out")
    context.driver.execute_script("arguments[0].click();", button1)


@then(u'Click on edit button in user_TA')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[8]/a[1]/img")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert new id and password in user info')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element(By.ID, "username").clear()
    context.driver.find_element(By.ID, "username").send_keys("ron")
    context.driver.find_element(By.ID, "password").clear()
    context.driver.find_element(By.ID, "password").send_keys("pat")


@then(u'Click on update button in user info')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_user")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify TUC login or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/p[1]").text
    print(txt)
    if txt == "Dashboard":
        assert True, "Login verify"
    else:
        assert False, "Login Failed"