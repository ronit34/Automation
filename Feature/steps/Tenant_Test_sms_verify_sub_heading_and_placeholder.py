from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Click on Test SMS')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_test_sms']/p")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder_Test_sms')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/p[2]").text

    if txt == "Test sending a new SMS of any type, all from one page.":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    sender_id = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div[1]/div[1]/input").get_attribute('placeholder')
    print(sender_id)
    if sender_id == "Enter Sender ID":
        assert True, f"{sender_id}"
    else:
        assert False, f"{sender_id}"

    recipient = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div[1]/div[2]/input").get_attribute('placeholder')
    print(recipient)
    if recipient == "Enter Recipient Number":
        assert True, f"{recipient}"
    else:
        assert False, f"{recipient}"

    pe_id = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div[2]/div[1]/input").get_attribute('placeholder')
    print(pe_id)
    if pe_id == "Enter PE ID":
        assert True, f"{pe_id}"
    else:
        assert False, f"{pe_id}"

    template_id = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div[2]/div[2]/input").get_attribute('placeholder')
    print(template_id)
    if template_id == "Enter Template ID":
        assert True, f"{template_id}"
    else:
        assert False, f"{template_id}"