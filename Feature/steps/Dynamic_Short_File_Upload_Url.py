import re
import pyperclip
from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import CommonUtility as CU

new_dynamic_sms_inputObj = CU.new_dynamic_sms_input()


@then(u'insert data into Dynamic short url')
def insert_dynamic(context):
    time.sleep(3)
    a=context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.NAME, "file1").send_keys("/home/onexadmin/Downloads/fileFormats/dynamic_csv/10Nos1Vars10VarLength.csv")
    time.sleep(1)
    context.driver.switch_to.default_content()

    for element_id in new_dynamic_sms_inputObj.new_unicode_sms_input_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_dynamic_sms_inputObj.new_unicode_sms_input_list[element_id])

    # select Text column
    # button = context.driver.find_element(By.XPATH,
    #         "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/div/div/div[1]/ul/li[1]")
    # button = context.driver.find_element(By.XPATH,
    #         "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[1]/ul/li[2]")
    # context.driver.execute_script("arguments[0].click();", button)

    # click on arrow
    # button = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/button[1]")
    # button = context.driver.find_element_by_xpath(
    #     "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/button[1]")
    # context.driver.execute_script("arguments[0].click();", button)

    # click on Insert Template template_name
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
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

    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Insert URL in dynamic')
def step_impl(context, googleSheet=None):
    # click on Insert URL
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_url")
    context.driver.execute_script("arguments[0].click();", button)

    # # select protocol
    time.sleep(3)
    button = context.driver.find_element(By.XPATH,
               "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[5]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/select")
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
