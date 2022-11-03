from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


@then(u'Click on choose csv file with special character name')
def step_impl(context):
    time.sleep(2)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys("/home/ronit/Desktop/official/Contabo/File format/NameWithSpecialCharacter/dynamic@@1k.csv")


@then(u'select columns for variable')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[1]/ul/li")
    context.driver.execute_script("arguments[0].click();", button)
    button1 = context.driver.find_element(By.XPATH, "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/button[1]")
    context.driver.execute_script("arguments[0].click();", button1)


@then(u'click on send now button for special char file')
def step_impl(context):
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)



