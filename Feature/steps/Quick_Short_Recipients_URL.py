import re

import pyperclip
from behave import *
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


@then(u'Insert Template')
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
    select.select_by_value("serv_imp")

    # select template as English short
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("One Variable")
    # select.select_by_value("1331")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Insert URL')
def step_impl(context, googleSheet=None):
    # click on Insert URL
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_url")
    context.driver.execute_script("arguments[0].click();", button)

    # # select protocol
    time.sleep(3)
    button = context.driver.find_element(By.XPATH,
               "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/select")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("https://")

    # enter target URL
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/div[2]/div/div/input").send_keys("www.onextel.com")

    # select get location checkbox
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/div[3]/label")
    context.driver.execute_script("arguments[0].click();", button)

    # click on Insert button
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/input[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # copy and paste url in place of {#var#}
    time.sleep(5)
    txt= context.driver.find_element_by_xpath("//*[@id='msgText']").get_attribute("value")
    print(f"{txt} is present")
    print(f"{txt} is present")

    a = (txt[24:])

    s1 = re.sub(a, "", txt)
    s2 = re.sub("{#var#}", a, s1)
    # txt.replace(txt, "{#var#}", a )
    s3 = str(s2)
    pyperclip.copy(s3)
    # s1 = re.sub(a, "", txt)

    # Element = context.driver.find_element_by_id("some_id")
    # Element.send_keys(Keys.CONTROL, 'v')
    # s2 = re.sub("{#var#}", a, s1)

    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='msgText']").clear()

    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='msgText']").send_keys(Keys.CONTROL, 'v')


# @then(u'Click on Send Button of quick sms')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element(By.ID, "send")
#     context.driver.execute_script("arguments[0].click();", button)
#
#     time.sleep(7)
#     button = context.driver.find_element(By.ID, "confirm_send_sms")
#     # button = context.driver.find_element(By.XPATH, "//*[@id='confirm_send_sms']")
#     context.driver.execute_script("arguments[0].click();", button)



