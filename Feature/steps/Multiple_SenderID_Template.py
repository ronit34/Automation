import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@then(u'Enter data to create new template')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("template_name").send_keys("New Template")
    time.sleep(1)
    context.driver.find_element_by_id("template_id").send_keys(98765)

    entity = context.driver.find_element(By.ID, "template_type_id")
    select = Select(entity)
    select.select_by_value("serv_imp")

    time.sleep(1)
    entity = context.driver.find_element(By.ID, "template_entity_id")
    select = Select(entity)
    select.select_by_visible_text("Onextel(123)")

    time.sleep(1)
    entity = context.driver.find_element(By.ID, "template_sender_id")
    select = Select(entity)
    select.select_by_value("PVRCIN")
    select.select_by_value("BHARAT")
    select.select_by_value("ZEPTON")

    time.sleep(1)
    context.driver.find_element_by_id("template_description").send_keys("Template using Multiple Sender ID")

    time.sleep(1)
    context.driver.find_element_by_id("template_content").send_keys("Its a test template")


@then(u'Check new template is created or not')
def step_impl(context):
    time.sleep(1)
    s1 = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[2]/td[3]").text
    s2 = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[3]/td[3]").text
    s3 = context.driver.find_element_by_xpath("//*[@id='template_table']/tbody/tr[4]/td[3]").text

    if s1 == "BHARAT" and s2 == "PVRCIN" and s3 == "ZEPTON":
        print(f"{s1}, {s2}, {s3} --> Sender IDs found")
        print(f"{s1}, {s2}, {s3} --> Sender IDs found")
    else:
        assert False, f"{s1}, {s2}, {s3} --->Sender IDs not found"

    # time.sleep(1)
    # context.driver.close()