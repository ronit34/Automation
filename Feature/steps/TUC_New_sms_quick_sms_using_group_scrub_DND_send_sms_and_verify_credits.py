import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Click on Phonebook and create a group and add DND contact')
def step_impl(context):
    time.sleep(2)
    # click on phonebook
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_phonebook']/p")
    context.driver.execute_script("arguments[0].click();", button)
    # click on add group and insert details for creating group
    btn_group = context.driver.find_element(By.ID, "add-group")
    context.driver.execute_script("arguments[0].click();", btn_group)
    context.driver.find_element(By.ID, "group-name").send_keys("test")
    context.driver.find_element(By.ID, "group-desc").send_keys("abcd")
    # add group
    add_group_button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", add_group_button)
    # click on contact
    contact_button = context.driver.find_element(By.ID, "contacts")
    context.driver.execute_script("arguments[0].click();", contact_button)
    # click on add contact
    add_contact_button = context.driver.find_element(By.ID, "add-contacts")
    context.driver.execute_script("arguments[0].click();", add_contact_button)
    # select bulk contact
    check_bulk_button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div["
                                                              "1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/input[2]")
    context.driver.execute_script("arguments[0].click();", check_bulk_button)
    # upload file for bulk contact
    context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/sms service/Scrub_DND_Campaignm.csv")
    # select group name

    select1 = Select(context.driver.find_element(By.ID, "select-group-bulk"))
    select1.select_by_visible_text('test(500)')
    # add contacts
    add_button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", add_button)


@then(u'Click on Select group')
def step_impl(context):
    select1 = Select(context.driver.find_element(By.ID, "groupDropdown"))
    select1.select_by_visible_text('test (4)')
