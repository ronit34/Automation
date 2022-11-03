import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Click on Quick Unicode SMS')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, "//*[@id='unicode_sms_page_link']/div/img[2]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert template in unicode')
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
    select.select_by_visible_text("Promo (2)")

    # select template as English short
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("Promo Hindi")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Check Allow Unicode')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div["
                                                   "2]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)