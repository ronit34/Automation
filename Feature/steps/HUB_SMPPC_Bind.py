import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@then(u'Click on Edit button in Action to enter details')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[5]/a[3]/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Select Carrier name as Airtel')
def step_impl(context):
    time.sleep(2)
    carrier = context.driver.find_element(By.ID, "carrier_id")
    select = Select(carrier)
    select.select_by_visible_text("AIRTEL")

@then(u'Select Vendor name as Airtel')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "vendor")
    select = Select(entity)
    # select.select_by_visible_text("Airtel")
    select.select_by_visible_text("vendor_AIRTEL")

@then(u'Select Circle name as Haryana in SMPPC')
def step_impl(context):
    time.sleep(2)
    circle = context.driver.find_element(By.ID, "circle_id")
    select = Select(circle)
    select.select_by_visible_text("Haryana")

@then(u'Select Circle name as Haryana')
def step_impl(context):
    time.sleep(2)
    vendor = context.driver.find_element(By.ID, "vendor")
    select = Select(vendor)
    select.select_by_visible_text("Airtel")

@then(u'Enter Primary Host/IP')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "host").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "host").send_keys("127.0.0.1")

@then(u'Enter Port Number')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "port").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "port").send_keys("5555")

@then(u'Select SMPP Bind Type')
def step_impl(context):
    time.sleep(2)
    bind = context.driver.find_element(By.ID, "mode")
    select = Select(bind)
    select.select_by_visible_text("TRANSCEIVER(TRX)")

@then(u'Click on update button to update bind data')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "update_smppc")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click on Bind button for bind')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[5]/a[1]/img")
    context.driver.execute_script("arguments[0].click();", button)
