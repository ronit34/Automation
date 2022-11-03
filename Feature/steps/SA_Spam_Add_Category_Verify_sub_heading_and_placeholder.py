import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Add Category')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "add-spam-cat")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder Create Spam Category')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div["
                                                "1]/p[2]").text
    if txt == "Add a new Category by filling the details below":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    category = context.driver.find_element(By.ID, "spam-cat-name").get_attribute('placeholder')
    if category == "Enter Category Name":
        assert True, f"{category}"
    else:
        assert False, f"{category}"
