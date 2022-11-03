import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Click on add group in phonebook')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "add-group")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert group details')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "group-name").send_keys("testgroup")
    context.driver.find_element(By.ID, "group-desc").send_keys("testing")


@then(u'Click on Contacts')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "contacts")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Add Contacts')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "add-contacts")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Choose Upload Bulk Contact')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div["
                                                   "2]/div/div/div/div/div/div[2]/div[1]/div/input[2]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Choose for upload a number file')
def step_impl(context):
    time.sleep(1)
    context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys("/home/ronit/Desktop/official/Contabo/File "
                                                          "format/phonebook_bulk/1k.csv")
    select = Select(context.driver.find_element(By.ID, "select-group-bulk"))
    select.select_by_visible_text("testgroup(501)")


@then(u'Click on close button in phonebook contact')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='addcontact']/div/div/div[1]/input")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Choose for upload again same number file')
def step_impl(context):
    time.sleep(1)
    context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys("/home/ronit/Desktop/official/Contabo/File "
                                                          "format/phonebook_bulk/1k.csv")
    select = Select(context.driver.find_element(By.ID, "select-group-bulk"))
    select.select_by_visible_text("testgroup(501)")


@then(u'Click on cancel button in phonebook contact')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", button)
