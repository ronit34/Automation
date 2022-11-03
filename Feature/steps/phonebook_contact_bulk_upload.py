import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@then(u'click on the Add contacts tab')
def click_add_contacts(context):
    time.sleep(1)
    # button = context.driver.find_element_by_id("create_contact")
    button = context.driver.find_element_by_id("add-contacts")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'select the Upload Bulk Contact option inside add contacts tab')
def select_option(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='addcontact']/div/div/div[2]/div[1]/div/label[2]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'choose the file to upload')
def choose_file(context):
    time.sleep(2)
    a = context.driver.switch_to.frame("up_onex_file")
    # context.driver.find_element_by_id("file1").send_keys("/home/administrator/Downloads/10.xlsx")
    # context.driver.find_element_by_id("file1").send_keys("/home/administrator/Downloads/1k.xlsx")
    # context.driver.find_element_by_id("file1").send_keys("/home/administrator/Downloads/10lac_apprx/1lac_a.csv")
    # context.driver.find_element_by_id("fisle1").send_keys("/home/administrator/Downloads/10lac_apprx/1lac_b.csv")
    # context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/fileFormats/csv_files/1lac.csv")
    context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/fileFormats/csv_files/100.csv")
    time.sleep(3)
    context.driver.switch_to.default_content()

@then(u'select the group to which you want to add contacts')
def select_group(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_xpath("//*[@id='select-group-bulk']"))
    # select.select_by_visible_text('xyz')
    # select.select_by_visible_text('abc')
    # select.select_by_visible_text('rty')
    # select.select_by_visible_text('npc')
    # select.select_by_visible_text('qwerty')
    select.select_by_visible_text('abcd(500)')

@then(u'finally click on add button')
def click_add_button(context):
    time.sleep(10)
    button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", button)
    # time.sleep(1)
    # context.driver.refresh()
    # time.sleep(1)
    # context.driver.close()
