from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import datetime
current_time = datetime.datetime.now()
from datetime import datetime,date
now = datetime.now()

@then(u'insert unicode data')
def step_impl(context):
    # click on Insert Template template_name
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("serv_imp")

    # select template as Hindi short
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    # select.select_by_value("1307")        #####Hindi One Var#####
    select.select_by_visible_text("Hindi One Variable")        ##### Hindi One Var #####

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on send button of unicode')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
             "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[1]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
             "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[2]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(2)
    # button = context.driver.find_element(By.ID, "proceed")
    # context.driver.execute_script("arguments[0].click();", button)
    #
    # time.sleep(2)
    # button = context.driver.find_element(By.ID, "confirm_send_sms")
    # context.driver.execute_script("arguments[0].click();", button)
    #
    # time.sleep(1)
    # context.driver.close()

