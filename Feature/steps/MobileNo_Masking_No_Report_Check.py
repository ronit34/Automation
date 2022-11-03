from behave import *
import time

@then(u'Check mobile Number is not masked')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[5]").text
    if txt == "9234567890":
        print(f"{txt} --> Mobile Number is not masked")
        print(f"{txt} --> Mobile Number is not masked")
    else:
        assert False, f"{txt} ---> Mobile Number is masked"

@then(u'check mobile number is not masked in search')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='search-table']/tbody/tr[2]/td[7]").text
    if text == "9234567890":
        print(f"{text} --> Mobile Number is not masked")
        print(f"{text} --> Mobile Number is not masked")
    else:
        assert False, f"{text}---> Mobile Number is masked"

    # time.sleep(1)
    # context.driver.close()