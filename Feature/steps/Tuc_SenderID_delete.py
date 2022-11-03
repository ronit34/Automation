from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'click on delete icon in SenderID')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id='senderid_table']/tbody/tr[2]/td[7]/a[2]").click()


@then(u'check labels in popup')
def step_impl(context):
    time.sleep(1)
    SenderID = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/div/div/div/div[2]/p[1]").text
    label = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/div/div/div/div[2]/p[2]").text

    if (SenderID == "Sender ID : 987654" and label == "Are you sure want to delete?"):
        assert True, f"{SenderID} --> label present"
    else:
        assert False, f"{SenderID} ----> label absent"