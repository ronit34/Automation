from behave import *
import time

from selenium.webdriver.support.ui import Select


# from selenium import webdriver

@then(u'select data from otp')
def step_impl(context):
    time.sleep(1)
    tuc = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/select")
    select = Select(tuc)
    select.select_by_value("204")


@then(u'select data from Service Implicit')
def step_impl(context):
    time.sleep(1)
    tuc = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[2]/select")
    select = Select(tuc)
    select.select_by_value("204")


@then(u'select data from Service Explicit')
def step_impl(context):
    time.sleep(1)
    tuc = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[3]/select")
    select = Select(tuc)
    select.select_by_value("204")


@then(u'select data from Promotional')
def step_impl(context):
    time.sleep(1)
    tuc = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[4]/select")
    select = Select(tuc)
    select.select_by_value("204")


@then(u'select data from TransPromo')
def step_impl(context):
    time.sleep(1)
    tuc = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[5]/select")
    select = Select(tuc)
    select.select_by_value("204")


@then(u'select data from Government Exempted')
def step_impl(context):
    time.sleep(1)
    tuc = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[6]/select")
    select = Select(tuc)
    select.select_by_value("204")


@then(u'select data from Simroute')
def step_impl(context):
    time.sleep(1)
    tuc = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[7]/select")
    select = Select(tuc)
    select.select_by_value("204")


@then(u'click on Save default gateway')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("save_default_gateways").click()


@then(u'click on okay')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("cancel").click()

    # time.sleep(1)
    # context.driver.close()