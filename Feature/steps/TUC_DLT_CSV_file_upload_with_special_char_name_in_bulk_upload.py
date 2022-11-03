from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


@then(u'choose csv file for jio operator')
def step_impl(context):
    time.sleep(2)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/official/Contabo/File format/NameWithSpecialCharacter/template@@BulkJio.csv")


@then(u'check message on popup')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/h5").text
    print(text)
    if text == "New Templates Added Successfully !!!":
        assert True, f"{text} -----> present"
    else:
        assert False, f"{text} -----> absent"
