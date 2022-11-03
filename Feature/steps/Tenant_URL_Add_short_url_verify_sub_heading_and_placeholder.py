from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Click on URL in tenant')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_url_tnt']/p")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder_Routing')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[1]/p[2]").text

    if txt == "Fill the below details to add a new short URL":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    url = context.driver.find_element(By.ID, "url_name").get_attribute('placeholder')
    print(url)
    if url == "Enter URL":
        assert True, f"{url}"
    else:
        assert False, f"{url}"