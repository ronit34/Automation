from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'insert long template data for dynamic')
def step_impl(context):
    # select columns
    button = context.driver.find_element(By.XPATH,
              "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[1]/ul/li[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # click on arrow
    button = context.driver.find_element_by_xpath(
        "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/button[1]")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("serv_imp")

    # select template as English Long
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("1301")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click on Allow MultiPart SMS')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[6]/div[1]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)
