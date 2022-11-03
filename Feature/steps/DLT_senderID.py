from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import CommonUtility as CU
DLTsenderIDObj = CU.DLT_senderID()

@then(u'click on Add sender id button')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "senderid_tab").click()
    time.sleep(1)
    button = context.driver.find_element(By.ID, "create_senderid")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check elements is present on page')
def step_impl(context):
    for x in DLTsenderIDObj.DLT_senderID_inputbox_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'Enter Id "{id}"')
def step_impl(context,id):
    context.driver.find_element(By.ID, "sender_name").send_keys(id)

@then(u'Select Entity Name "{name}"')
def entity(context,name):
    entity = context.driver.find_element(By.ID, "sender_entity_id")
    select = Select(entity)
    select.select_by_visible_text(name)


@then(u'Click on Add')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "add_sender_id").click()

@then(u'check sender id is created or not')
def sender(context):
    time.sleep(1)
    sender = context.driver.find_element(By.XPATH, "//*[@id='senderid_table']/tbody/tr[2]/td[1]").text
    if (sender == "123456"):
        assert True, f"{sender} found"
    else:
        assert False, f"Sender ID {sender} not found"

    # time.sleep(2)
    # context.driver.close()


