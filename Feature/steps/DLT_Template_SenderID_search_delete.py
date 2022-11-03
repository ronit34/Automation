from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Enter Data to create Entity')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("entity_id").send_keys(456)
    time.sleep(1)
    context.driver.find_element_by_id("entity_name").send_keys("OTPL")


@then(u'Enter data to create template')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("template_name").send_keys("Test Template")
    time.sleep(1)
    context.driver.find_element_by_id("template_id").send_keys(45678)

    entity = context.driver.find_element(By.ID, "template_type_id")
    select = Select(entity)
    select.select_by_value("serv_imp")

    time.sleep(1)
    entity = context.driver.find_element(By.ID, "template_entity_id")
    select = Select(entity)
    select.select_by_visible_text("OTPL(456)")

    time.sleep(1)
    entity = context.driver.find_element(By.ID, "template_sender_id")
    select = Select(entity)
    select.select_by_value("987654")

    time.sleep(1)
    context.driver.find_element_by_id("template_description").send_keys("Test Delete")

    time.sleep(1)
    context.driver.find_element_by_id("template_content").send_keys("It's a test template")


@then(u'Enter Sender Id "987654"')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("sender_name").send_keys(987654)


@then(u'Select the Entity Name')
def step_impl(context):
    entity = context.driver.find_element(By.ID, "sender_entity_id")
    select = Select(entity)
    select.select_by_visible_text("OTPL(456)")


@then(u'input senderID in template to search')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='senderid-template']").clear()
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='senderid-template']").send_keys("987654")
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'click on delete template')
def step_impl(context):
    time.sleep(1)
    # button = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[8]/a[2]/img")
    button = context.driver.find_element(By.XPATH,
                "//*[@id='template_table']/tbody/tr[2]/td[9]/a/img")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'click on delete of sender id')
def step_impl(context):
    time.sleep(1)
    # button = context.driver.find_element(By.XPATH, "//*[@id='senderid_table']/tbody/tr[2]/td[7]/a[2]/img")
    button = context.driver.find_element(By.XPATH,
                "//*[@id='senderid_table']/tbody/tr[4]/td[7]/a[2]/img")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'click on entity tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "entityid_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'click on delete of entity id')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                "//*[@id='entityid_table']/tbody/tr[3]/td[3]/a[2]/img")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()

