import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Click on Add Tenant')
def step_impl(context):
    button = context.driver.find_element(By.ID, "create_tenant")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert details of growtel')
def step_impl(context):
    context.driver.find_element(By.ID, "name").send_keys("Growtel")
    context.driver.find_element(By.ID, "description").send_keys("abc")
    context.driver.find_element(By.ID, "childtuc").send_keys("1")
    context.driver.find_element(By.ID, "smpps").send_keys("1")
    context.driver.find_element(By.ID, "smsapi").send_keys("1")


@then(u'Click on create tenant')
def step_impl(context):
    button = context.driver.find_element(By.ID, "save_tenant")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert details for growtel')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("growtelronit")
    context.driver.find_element(By.ID, "password").send_keys("growtelronit")
    context.driver.find_element(By.ID, "fname").send_keys("Ronit")
    context.driver.find_element(By.ID, "lname").send_keys("Patel")
    context.driver.find_element(By.ID, "email").send_keys("ronit.patel@onextel.tech")
    context.driver.find_element(By.ID, "mob_no").send_keys("7008427274")
    context.driver.find_element(By.ID, "comp_name").send_keys("ONEXTEL")
    context.driver.find_element(By.ID, "web").send_keys("onextel.com")
    context.driver.find_element(By.ID, "other_mob_no").send_keys("7008427274")
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "role_type"))
    select.select_by_visible_text("Tenant Admin")
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "tenant"))
    select.select_by_visible_text("Growtel(12)")

    button2 = context.driver.find_element(By.ID, "save_user")
    context.driver.execute_script("arguments[0].click();", button2)