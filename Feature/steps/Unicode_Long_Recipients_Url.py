import re

import pyperclip
from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then(u'Insert hindi long var Template')
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
    select.select_by_visible_text("Hindi Long")

    time.sleep(2)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert URL for unicode long')
def step_impl(context):
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
    button = context.driver.find_element(By.XPATH,
                                         "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[1]/div[3]/label")
    context.driver.execute_script("arguments[0].click();", button)

    # click on Insert button
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[2]/div[2]/input[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # copy and paste url in place of {#var#}
    time.sleep(3)
    txt = context.driver.find_element_by_xpath("//*[@id='msgText']").get_attribute("value")
    print(f"{txt} is present")
    print(f"{txt} is present")

    a = (txt[418:])
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

    #Code Checking for send
    # creds = context.driver.find_element_by_xpath("//*[@id='available_credits']").text
    # credits = int(creds.replace(',', ''))

    # time.sleep(1)
    # button = context.driver.find_element(By.ID, "send")
    # context.driver.execute_script("arguments[0].click();", button)

@then(u'we are trying to send sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

        # try:
        #     WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.ID, "confirm_send_sms")))
        #     print("Button located")
        #     print("Button located")
        #
        # except:
        #     pass
        # print("Button not ready to be clicked!")
        # print("Button not ready to be clicked!")

    # element = WebDriverWait(context.driver, 20).until(
    #
    #     EC.presence_of_element_located((By.ID, "confirm_send_sms")))
    # time.sleep(4)
    # element = WebDriverWait(context.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='confirm_send_sms']"))).click()
    # time.sleep(2)
    # button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[3]/input[2]")
    # context.driver.execute_script("arguments[0].click();", button)






























# @then(u'click on allow unicode and multi part checkbox')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[1]/label[1]/input")
#     context.driver.execute_script("arguments[0].click();", button)
#
#     button = context.driver.find_element_by_xpath(
#         "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[2]/label[1]/input")
#     context.driver.execute_script("arguments[0].click();", button)
