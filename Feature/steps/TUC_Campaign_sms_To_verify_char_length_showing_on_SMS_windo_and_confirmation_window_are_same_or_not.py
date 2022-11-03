from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


@then(u'Count characters')
def count_char(context):
    time.sleep(2)
    text_2 = context.driver.find_element(By.ID, "limit_msg").text
    list_ = text_2.split(" ")
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='msgText']").get_attribute("value")
    list_2 = list(txt)
    length_1 = len(list_2)
    var = "{" and "}"
    for i in list_2:
        if i in var:
            length_1 += 2
    count_length = length_1
    context.char = int(list_[0])

    if context.char == count_length:
        assert True, "Passed"
    else:
        assert False, "Failed"


@then(u'Verify char length showing on SMS windo and confirmation window are same or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH,
                                      "//*[@id='dashboard']/div[2]/div[1]/div[3]/div[2]/div[2]/div[8]/div/p").text
    if context.char == int(txt):
        assert True, "Passed"
    else:
        assert False, "Failed"
