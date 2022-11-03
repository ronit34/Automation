from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


@then(u'Select jio operator')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "bulk-operator")
    select = Select(entity)
    select.select_by_visible_text("Jio")


@then(u'choose file for jio_sender_id_missing_file')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/official/Contabo/File format/Bulk_template_rk/jio/jio_missing_senderid.csv")


@then(u'Click on save templates')
def step_impl(context):
    time.sleep(5)
    context.driver.switch_to.default_content()
    button = context.driver.find_element(By.ID, "bulk-save")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check sender_id Failed missing popup')
def step_impl(context):
    time.sleep(10)
    text = context.driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/h5").text
    if text == "One or more Header/SenderID are empty!! Please Check File!!":
        assert True, f"{text} Present"
    else:
        assert False, f"{text} Absent"


@then(u'click on OK button in bulk_upload')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "ok_modal").click()
    time.sleep(5)


@then(u'choose file for template_id_missing_file')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/official/Contabo/File format/Bulk_template_rk/jio/jio_missing_tempID.csv")


@then(u'check error file content invalid')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div[2]/div/div[1]/h5").text
    if text == "Error":
        assert True, f"{text} Present"
    else:
        assert False, f"{text} Absent"
    context.driver.refresh()


@then(u'choose file for template_name_missing_file')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/official/Contabo/File format/Bulk_template_rk/jio/jio_missing_temp_name.csv")


@then(u'check template_name already exist')
def step_impl(context):
    time.sleep(10)
    text = context.driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/h5").text
    if text == "3 Templates from the file already exists !!!":
        assert True, f"{text} Present"
    else:
        assert False, f"{text} Absent"


@then(u'choose file for template_type_missing_file')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/official/Contabo/File format/Bulk_template_rk/jio/jio_missing_temp_type.csv")


@then(u'choose file for jio')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element(By.ID, "file1").send_keys(
        "/home/ronit/Desktop/official/Contabo/File format/Bulk_template_rk/jio/templateBulkJio.csv")
