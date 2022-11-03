from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


@then(u'Insert group name and description')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "group-name").send_keys("specialchartest")
    context.driver.find_element(By.ID, "group-desc").send_keys("abcd")


@then(u'Click on Add in add group of phonebook')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "add").click()


@then(u'click on the Add contacts tab in phonebook')
def click_add_contacts(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "add-contacts")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'select the Upload Bulk Contact option inside add contacts tab in phonebook')
def select_option(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='addcontact']/div/div/div[2]/div[1]/div/label[2]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'choose the file to upload csv file')
def step_impl(context):
    time.sleep(2)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/official/Contabo/File format/NameWithSpecialCharacter/campaign@@10.csv")


@then(u'select the group to which you want to add contact')
def step_impl(context):
    select1 = Select(context.driver.find_element(By.ID, "select-group-bulk"))
    select1.select_by_visible_text('specialchartest(500)')
