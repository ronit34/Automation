
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import CommonUtility as CU


@then(u'Enter data to create 1st temp1')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "template_name").send_keys("Sample template 1")
    context.driver.find_element(By.ID, "template_id").send_keys("121212")
    time.sleep(1)
    element_obj = context.driver.find_element(By.ID, "template_type_id")
    select = Select(element_obj)
    select.select_by_visible_text("Service Implicit")

    time.sleep(1)
    element_obj = context.driver.find_element(By.ID, 'template_sender_id')
    select = Select(element_obj)
    select.select_by_visible_text("987654")

    time.sleep(1)
    context.driver.find_element(By.ID, "template_description").send_keys(" this is a sample template 1")
    time.sleep(1)
    context.driver.find_element(By.ID, "template_content").send_keys("I love ice creams")


@then(u'Enter data to create second temp2')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "template_name").send_keys("Sample template 2")
    context.driver.find_element(By.ID, "template_id").send_keys("112211")
    time.sleep(1)
    element_obj = context.driver.find_element(By.ID, "template_type_id")
    select = Select(element_obj)
    select.select_by_visible_text("Service Implicit")

    time.sleep(1)
    element_obj = context.driver.find_element(By.ID, 'template_sender_id')
    select = Select(element_obj)
    select.select_by_visible_text("987654")

    time.sleep(1)
    context.driver.find_element(By.ID, "template_description").send_keys(" this is a sample template 2")
    time.sleep(1)
    context.driver.find_element(By.ID, "template_content").send_keys("I love puddings")


@then(u'check edit icon mouse hover text - template')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[2]/td[8]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[2]/td[8]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on edit icon in temp1')
def step_impl(context):
    time.sleep(4)
    button = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[9]/td[8]/a[1]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'change the field data')
def step_impl(context):
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[1]/input").clear()
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[1]/input").send_keys("Edited template")
    time.sleep(1)
    context.driver.find_element(By.ID, "template_id").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "template_id").send_keys("11111111")


@then(u'click on update to save changes')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[3]/input[2]").click()


@then(u'check the updated changes')
def step_impl(context):
    time.sleep(2)
    template = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[9]/td[2]").text
    if (template == "Edited template"):
        assert True, f"{template} found"
    else:
        assert False, f"{template} not found"

@then(u'select the check box of the template')
def step_impl(context):
    time.sleep(4)
    context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[9]/td[1]/label/input").click()


