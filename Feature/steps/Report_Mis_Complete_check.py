import math
from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU


@then(u'fill Wrong Sender ID')
def step_impl(context):
    context.driver.find_element_by_id("web_senderid").send_keys("1234567")

    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-daily-summary']/div[3]").text
    if text == "No report data avaialable":
        assert True, "No data for this Sender ID"
    else:
        assert False, f"{text} is not present"
    time.sleep(2)
    context.driver.refresh()


@then(u'fill Correct Sender ID')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("web_senderid").send_keys("123456")

    # change default limit 20 to 100
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('page_record_limit'))
    select.select_by_value('100')

    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'set limit and check pagination')
def step_impl(context):
    time.sleep(2)    ## finding rows on 1st page
    rows_len1 = len(context.driver.find_elements_by_xpath(
                   "//*[@id='customers']/tbody/tr")) - 1
    # print(f"{rows_len1} --> is present")
    # print(f"{rows_len1} --> is present")

    time.sleep(1)  ## clicking on Next to go to other page
    button = context.driver.find_element(By.XPATH,
              "//*[@id='pills-daily-summary']/div[3]/nav/a[2]")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)  ## finding rows on 2nd page
    rows_len2 = len(context.driver.find_elements_by_xpath(
        "//*[@id='customers']/tbody/tr")) - 1
    # print(f"{rows_len2} --> is present")
    # print(f"{rows_len2} --> is present")

    rows_len = rows_len1 + rows_len2  ## finding total rows of page 1 & page 2
    # print(f"{rows_len} --> is present")
    # print(f"{rows_len} --> is present")

    length = rows_len / 5
    final_length = math.ceil(length)
    # print(f"{final_length} --> is present")
    # print(f"{final_length} --> is present")


    ############# Set Limit ###########################
    time.sleep(2)
    select = Select(context.driver.find_element_by_id('page_record_limit'))
    select.select_by_value('5')
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

    #############VERIFY NO OF RECORDS AFTER LIMIT #################

    time.sleep(1)
    limit_len = len(context.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr")) - 1

    if limit_len == 5:
        assert True, "no of record  verified"
    elif 5 > limit_len > 0:
        print("Less than 5 records")
    else:
        assert False, f"{limit_len} is the length of records after limit"

    ############ VERIFY NO OF PAGINATION #################

    time.sleep(1)
    str_le = str(final_length)
    rows_len = str(rows_len)
    page = context.driver.find_element_by_xpath("//*[@id='pills-daily-summary']/div[3]/nav/a").text
    if page == "Page 1 of " + str_le + "(Total Records:" + rows_len + ")":
        assert True, f"{page} is present"
    else:
        # print(f"{page} --> is present")
        # print(f"{page} --> is present")
        assert False, f"{page} , {str_le} , {rows_len}---->not present"


@then(u'click on action icon')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[2]/td[14]/a")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'verify submitted count')
def step_impl(context):
    Sub = context.driver.find_element_by_xpath("//*[@id='v-pills-tab']/div[1]/p[2]").text
    # Sub = context.driver.find_element_by_xpath("//*[@id='senderid-summary-table']/tbody/tr[2]/td[3]").text
    Del = context.driver.find_element_by_xpath("//*[@id='v-pills-tab']/div[2]/p[2]").text
    # Del = context.driver.find_element_by_xpath("//*[@id='senderid-summary-table']/tbody/tr[2]/td[4]").text
    Fail = context.driver.find_element_by_xpath("//*[@id='v-pills-tab']/div[3]/p[2]").text
    # Fail = context.driver.find_element_by_xpath("//*[@id='senderid-summary-table']/tbody/tr[2]/td[5]").text
    Await = context.driver.find_element_by_xpath("//*[@id='v-pills-tab']/div[4]/p[2]").text
    # Await = context.driver.find_element_by_xpath("//*[@id='senderid-summary-table']/tbody/tr[2]/td[6]").text
    S = int(Sub)
    D = int(Del)
    F = int(Fail)
    A = int(Await)
    x = int(S - (D + F))
    if x == A:
        assert True, "count is verified"
    else:
        assert False, f"{A} count mismatch"


@then(u'enter mobile number')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("mobile").send_keys("1234567890")


@then(u'click on search in web detail')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check for zero count')
def step_impl(context):
    Del = context.driver.find_element_by_xpath("//*[@id='v-pills-tab']/div[2]/p[2]").text
    Fail = context.driver.find_element_by_xpath("//*[@id='v-pills-tab']/div[3]/p[2]").text
    Await = context.driver.find_element_by_xpath("//*[@id='v-pills-tab']/div[4]/p[2]").text
    D = int(Del)
    F = int(Fail)
    A = int(Await)

    if D == 0:
        select = Select(context.driver.find_element_by_id('status'))
        select.select_by_value('delivered')
        time.sleep(1)
        button = context.driver.find_element(By.ID, "search")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[3]").text
        if text == "No report data avaialable":
            assert True, f"{text}  text found"
        else:
            assert False, f"{text} not found"

        time.sleep(2)
        select = Select(context.driver.find_element_by_id('status'))
        select.select_by_value('all')
        time.sleep(1)
        button = context.driver.find_element(By.ID, "search")
        context.driver.execute_script("arguments[0].click();", button)


    elif F == 0:
        select = Select(context.driver.find_element_by_id('status'))
        select.select_by_value('failed')
        time.sleep(1)
        button = context.driver.find_element(By.ID, "search")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[3]").text
        if text == "No report data avaialable":
            assert True, f"{text}  text found"
        else:
            assert False, f"{text} not found"

        time.sleep(2)
        select = Select(context.driver.find_element_by_id('status'))
        select.select_by_value('all')
        time.sleep(1)
        button = context.driver.find_element(By.ID, "search")
        context.driver.execute_script("arguments[0].click();", button)

    elif A == 0:
        select = Select(context.driver.find_element_by_id('status'))
        select.select_by_value('awaited')

        time.sleep(1)
        button = context.driver.find_element(By.ID, "search")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[3]").text
        if text == "No report data avaialable":
            assert True, f"{text}  text found"
        else:
            assert False, f"{text} not found"

        time.sleep(2)
        select = Select(context.driver.find_element_by_id('status'))
        select.select_by_value('all')
        time.sleep(1)
        button = context.driver.find_element(By.ID, "search")
        context.driver.execute_script("arguments[0].click();", button)

    else:
        assert True


@then(u'select Status(Delivered)')
def step_impl(context):
    select = Select(context.driver.find_element_by_id('status'))
    select.select_by_value('delivered')


@then(u'select Status(Failed)')
def step_impl(context):
    select = Select(context.driver.find_element_by_id('status'))
    select.select_by_value('failed')

@then(u'select Status (Awaited)')
def step_impl(context):
    select = Select(context.driver.find_element_by_id('status'))
    select.select_by_value('awaited')

@then(u'set status to all')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('status'))
    select.select_by_value('all')
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'select Download file type in action')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div[2]/div/ul/li[1]/a")
    context.driver.execute_script("arguments[0].click();", button)
