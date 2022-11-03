import time
from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Update credits and add few credits point')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_balance")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    context.driver.find_element(By.ID, "amount").send_keys("10000")
    time.sleep(1)
    button1 = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", button1)


@then(u'Click on Credit')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_credit_allocation']/p")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Select Onexmedia and add credits')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "select_tuc"))
    select.select_by_visible_text("Onexmedia(10)")
    time.sleep(2)
    button1 = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div["
                                                    "2]/div/div/div/div/div/div[2]/div[4]/div/div[1]/input")
    context.driver.execute_script("arguments[0].click();", button1)
    context.driver.find_element(By.ID, "credits_amount").send_keys("10000")
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_credits")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on user profile')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='profile']/div/p[1]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on logout')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "log-out")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)


@then(u'Select ICICI and add credits')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "select_tuc"))
    select.select_by_visible_text("ICICI(2000)")
    button1 = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div["
                                                    "2]/div/div/div/div/div/div[2]/div[4]/div/div[1]/input")
    context.driver.execute_script("arguments[0].click();", button1)
    context.driver.find_element(By.ID, "credits_amount").send_keys("10000")
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_credits")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify token add or not')
def step_impl(context):
    time.sleep(1)
    txt = context.driver.find_element(By.ID, "available_credits").text
    if txt == "10,000":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"


@then(u'Close Window Driver')
def step_impl(context):
    time.sleep(2)
    context.driver.close()
