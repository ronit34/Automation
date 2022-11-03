from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'choose xls file for jio operator')
def step_impl(context):
    time.sleep(2)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/official/Contabo/File format/NameWithSpecialCharacter/template@@BulkJio.xls")

