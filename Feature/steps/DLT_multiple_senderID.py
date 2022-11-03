from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

@then(u'create multiple senderid')
def step_impl(context):
    ## 2nd Sender ID ##
    time.sleep(1)
    context.driver.find_element(By.ID, "sender_name").send_keys("BHARAT")

    entity = context.driver.find_element(By.ID, "sender_entity_id")
    select = Select(entity)
    select.select_by_visible_text("Onextel(123)")

    context.driver.find_element(By.ID, "add_sender_id").click()

    ## 3rd Sender ID ##
    time.sleep(1)
    button = context.driver.find_element(By.ID, "create_senderid")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element(By.ID, "sender_name").send_keys("JIOINF")

    entity = context.driver.find_element(By.ID, "sender_entity_id")
    select = Select(entity)
    select.select_by_visible_text("Onextel(123)")

    context.driver.find_element(By.ID, "add_sender_id").click()

    ## 4th Sender ID ##
    time.sleep(1)
    button = context.driver.find_element(By.ID, "create_senderid")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element(By.ID, "sender_name").send_keys("ZEPTON")

    entity = context.driver.find_element(By.ID, "sender_entity_id")
    select = Select(entity)
    select.select_by_visible_text("Onextel(123)")

    context.driver.find_element(By.ID, "add_sender_id").click()

    ## 5th Sender ID ##
    time.sleep(1)
    button = context.driver.find_element(By.ID, "create_senderid")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element(By.ID, "sender_name").send_keys("PVRCIN")

    entity = context.driver.find_element(By.ID, "sender_entity_id")
    select = Select(entity)
    select.select_by_visible_text("Onextel(123)")

    context.driver.find_element(By.ID, "add_sender_id").click()

    # time.sleep(1)
    # context.driver.close()



