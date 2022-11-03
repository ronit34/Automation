import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Keywords')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "spam_keywords")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder Add Span Keywords')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div["
                                                "1]/p[2]").text
    if txt == "Add new Keyword/Keywords by filling the details below":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    category = context.driver.find_element(By.ID, "spam-keyword").get_attribute('placeholder')
    if category == "Enter Keyword":
        assert True, f"{category}"
    else:
        assert False, f"{category}"
