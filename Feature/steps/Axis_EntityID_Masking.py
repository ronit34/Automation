from behave import *
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

import CommonUtility as CU

DLT_entityIDObj1 = CU.DLT_entityID_masked()

DLT_templateIDObj = CU.DLT_templateID()
DLT_templateID_mask_dropdownobj = CU.DLT_templateID_dropdown_masking()


@then(u'check entity id created with 3 digits')
def step_impl(context):
    time.sleep(1)
    entity = context.driver.find_element(By.XPATH, "//*[@id='entityid_table']/tbody/tr[2]/td[1]").text
    if (entity == "123"):
        assert True, f"{entity} found"
    else:
        assert False, f"{entity} not found"


@then(u'Insert data into entity fields (more than 3 digits)')
def step_impl(context):
    for element_id in DLT_entityIDObj1.DLT_entityID_masked_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            DLT_entityIDObj1.DLT_entityID_masked_inputbox_list[element_id])
        print(f"{element_id}")


@then(u'check entity id is masked or not')
def step_impl(context):
    time.sleep(1)
    entity2 = context.driver.find_element(By.XPATH, "//*[@id='entityid_table']/tbody/tr[2]/td[1]").text
    if (entity2 == "12**56"):
        assert True, f"{entity2} ----->found"
    else:
        assert False, f"{entity2} ------>not found"


@then(u'check entityID masked in created senderID')
def step_impl(context):
    time.sleep(1)
    entity3 = context.driver.find_element(By.XPATH, "//*[@id='senderid_table']/tbody/tr[2]/td[2]").text
    if (entity3 == "12**56"):
        assert True, f"{entity3} ----->found"
    else:
        assert False, f"{entity3} ------>not found"


@then(u'Enter the data into templateid fields(masking)')
def step_impl(context):
    for element_id in DLT_templateIDObj.DLT_templateID_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            DLT_templateIDObj.DLT_templateID_inputbox_list[element_id])
        print(f"{element_id}")

    for element_id in DLT_templateID_mask_dropdownobj.DLT_templateID_dropdown_masking_inputbox_list.keys():
        try:
            context.driver.implicitly_wait(20)
            element_obj = context.driver.find_element(By.ID, element_id)
            context.driver.implicitly_wait(20)
            select = Select(element_obj)
            context.driver.implicitly_wait(20)
            select.select_by_visible_text(
                DLT_templateID_mask_dropdownobj.DLT_templateID_dropdown_masking_inputbox_list[element_id])

        except NameError:
            print(NameError)

    time.sleep(2)
    entity = context.driver.find_element(By.ID, "template_sender_id")
    select = Select(entity)
    select.select_by_visible_text("123456")


#######################################################################################33


@then(u'select masked EntityID in bulk upload')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "bulktemplate_entity_id")
    select = Select(entity)
    select.select_by_visible_text("OneTech(12**56)")


@then(u'select operator in bulk upload')
def step_impl(context):
    time.sleep(2)
    entity = context.driver.find_element(By.ID, "bulk-operator")
    select = Select(entity)
    # select.select_by_visible_text("Airtel")
    # select.select_by_visible_text("Jio")
    # select.select_by_visible_text("Vodafone")
    select.select_by_visible_text("Vodafone/VI")


@then(u'select file in bulk upload')
def step_impl(context):
    time.sleep(3)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys("/home/onexadmin/Downloads/templateBulkVodafone.csv")


@then(u'Click on okay button to save temp')
def step_impl(context):
    time.sleep(1)
    context.driver.switch_to.default_content()
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div/div/div[2]/h5").text
    if (text == "New Templates Added Successfully !!!"):
        context.driver.find_element_by_id("ok_modal").click()
    else:
        assert False, "Text Failed"


@then(u'check masked entityID after bulk upload')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[3]/td[4]").text
    text2 = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[4]/td[4]").text

    if text == "12**56" and text2 == "12**56":
        assert True, f"{text} ----->masking verified"
    else:
        assert False, f"{text} ------>masking failed"

        #######################   search tab ###################################


@then(u'input template Name')
def step_impl(context):
    time.sleep(1)
    search_text = context.driver.find_element(By.ID, "enter_type").send_keys("English Long")


@then(u'select template name from dd')
def step_impl(context):
    time.sleep(2)
    temp = context.driver.find_element(By.ID, "template_type")
    select = Select(temp)
    select.select_by_visible_text("Template Name")


@then(u'check masked entityID in search tab')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[3]").text

    if text == "12**56":
        assert True, f"{text} ----->masking verified"
    else:
        assert False, f"{text} ------>masking failed"

    # time.sleep(2)
    # context.driver.close()
