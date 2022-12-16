import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Enter template id in template-')
def step_impl(context):
    context.driver.find_element(By.ID, "search-id").send_keys("1234567890")


@then(u'Click on set limit and check pagination working or not-')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "template_limit"))
    select.select_by_visible_text("5")

    time.sleep(2)
    Button1 = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", Button1)

    time.sleep(2)
    Button = context.driver.find_element(By.XPATH, "//*[@id='tab_content']/nav/a[2]")
    context.driver.execute_script("arguments[0].click();", Button)