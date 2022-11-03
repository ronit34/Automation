import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'enter data in search bar "{data}"')
def step_impl(context, data):
    context.driver.find_element_by_id("tuc_input").send_keys(data)

@then(u'click on search button in tuc')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "user_search")
    context.driver.execute_script("arguments[0].click();", button)

# @then(u'verify search in table')
# def step_impl(context):
#     time.sleep(2)
    # text = context.driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/td/tr").text
    # for td in context.driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/td"):
    #     if "hhhhh" in td.text:
    #         print(f"{td} ---haha")
    #         print(f"{td} ---haha")
    #     else:
    #         assert False, f"No tuc found with name sales"
    # my_element = context.driver.find_element_by_xpath(
    #     "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/td/tr[1]").text
    # # my_element = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/td/tr[contains(text(), 'sales')]")
    # print(f"{my_element}")
    # my_element.contains_text("sales")
    # time.sleep(2)
    # print(f"{my_element}")
    # print(f"{my_element}")
    # print(f"{my_element}")

@then(u'click on download file')
def step_impl(context):
    # click on Download button
    time.sleep(2)
    button = context.driver.find_element(By.ID, "dropdownMenuLink")
    context.driver.execute_script("arguments[0].click();", button)
    # context.driver.find_element(By.ID, "dropdownMenuLink").click()


#
#
@then(u'select file type to download')
def step_impl(context):
    time.sleep(2)
    # Selecting option for download file
    button = context.driver.find_element(By.ID, "download_csv")
    context.driver.execute_script("arguments[0].click();", button)
