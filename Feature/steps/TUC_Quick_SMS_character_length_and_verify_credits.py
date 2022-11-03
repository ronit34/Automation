from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


@then(u'select new_group for quick')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "groupDropdown"))
    select.select_by_visible_text('campaign (1)')


@then(u'Count character and credits')
def step_impl(context):
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

    # print(type(count_length))
    # print(type(list_[0]))

    if count_length <= 160:
        credit = 1
    elif count_length <= 306:
        credit = 2
    elif count_length <= 459:
        credit = 3
    elif count_length <= 612:
        credit = 4
    else:
        assert False, "Needs to add more length"

    if int(list_[0]) == count_length and int(list_[2]) == credit:
        assert True, "Passed"
    else:
        assert False, "Failed"


