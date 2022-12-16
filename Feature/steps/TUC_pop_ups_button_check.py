import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Verify insert template pop-ups and button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button1 = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button1)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[2]/p[1]/span").text
    if txt == "Mandatory":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Verify insert URL and button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_url")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[2]/p").text
    if txt == "Please Insert Template ID First!!!":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    button1 = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", button1)


@then(u'Verify Campaign description pop-up')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[3]/a/img")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[2]/p").text
    if txt == "this is default campaign.":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    ok_button = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Verify Action edit pop-up and delete pop-up')
def step_impl(context):
    time.sleep(1)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='campaign_edit']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    time.sleep(1)
    context.driver.find_element(By.ID, "campaign_name").clear()
    update_button = context.driver.find_element(By.ID, "update_campaign")
    context.driver.execute_script("arguments[0].click();", update_button)
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[1]/span/span").text
    if txt == "Please Enter Campaign Name":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)
    time.sleep(1)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']"
                                                          "/div[2]/table/tbody/tr[2]/td[4]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/div/div/div/div[2]/p[2]").text
    if txt == "Are you sure want to delete?":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "delete_cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on Add Campaigns')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "campaign_create")
    context.driver.execute_script("arguments[0].click()", button)
    

@then(u'Verify Add campaign')
def step_impl(context):
    time.sleep(2)
    add_button = context.driver.find_element(By.ID, "add_campaign")
    context.driver.execute_script("arguments[0].click();", add_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[1]/span/span").text
    if txt == "Please Enter Campaign Name":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on delete button and verify pop-up in TUC')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[2]/img")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div/div[2]/p[2]").text
    if txt == "Are you sure want to delete?":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "delete_cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on User in User management')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "user_view")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on delete button and verify pop-up in User')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[8]/a[2]/img")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div/div[2]/p[2]").text
    if txt == "Are you sure want to delete?":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "delete_cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on Update Credit in TUC')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "update_credit")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify update credit pop-up and update and cancel button')
def step_impl(context):
    time.sleep(1)
    update_button = context.driver.find_element(By.ID, "update_credits")
    context.driver.execute_script("arguments[0].click();", update_button)
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[2]/span/span").text
    if txt == "TUC not selected":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Entity ID Action tab click on edit button and verify pop-up')
def step_impl(context):
    time.sleep(2)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='edit_entityid123']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    time.sleep(1)
    context.driver.find_element(By.ID, "entity_name").clear()
    update_button = context.driver.find_element(By.ID, "update_entityid")
    context.driver.execute_script("arguments[0].click();", update_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                "div[1]/div[2]/div/div/div/div[2]/div[2]/span/span").text
    if txt == "Please Enter Entity Name":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Entity ID Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(2)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='entityid_table']/tbody/tr[2]/td[3]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    ok_button = context.driver.find_element(By.ID, "delete")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Click on Add Entity ID')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "create_entityid")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Entity id pop-up and add and cancel button')
def step_impl(context):
    time.sleep(2)
    add_button = context.driver.find_element(By.ID, "add_entityid")
    context.driver.execute_script("arguments[0].click();", add_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[1]/span[1]/span").text
    if txt == "Please Enter Entity Id":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on Sender IDs')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "senderid_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Sender IDs Action tab click on edit button and verify pop-up')
def step_impl(context):
    time.sleep(2)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='senderedit_123456']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Edit Sender ID":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Sender IDs Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(2)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='senderid_table']/tbody/tr[2]/td[7]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    ok_button = context.driver.find_element(By.ID, "delete")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Click on Add Sender ID')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "create_senderid")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sender id pop-up and add and cancel button')
def step_impl(context):
    time.sleep(1)
    add_button = context.driver.find_element(By.ID, "add_sender_id")
    context.driver.execute_script("arguments[0].click();", add_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[2]/span/span").text
    if txt == "Sender ID must contain only numbers-[0-9] or letters-[A-Z:a-z]":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on add template')
def step_impl(context):
    time.sleep(2)
    add_button = context.driver.find_element(By.ID, "create_template")
    context.driver.execute_script("arguments[0].click();", add_button)


@then(u'Verify template pop-up and add and cancel button')
def step_impl(context):
    time.sleep(2)
    add_button = context.driver.find_element(By.ID, "add_template")
    context.driver.execute_script("arguments[0].click();", add_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[1]/span/span").text
    if txt == "Template Name must be atleast 4 characters long":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on delete selected')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "delete_template")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify delete selected pop-up and ok and cancel button')
def step_impl(context):
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    ok_button = context.driver.find_element(By.ID, "delete")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Click on delete all')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "delete_all_template")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify delete all pop-up and cancel button')
def step_impl(context):
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div[2]/p[2]").text
    if txt == "Are you sure you want to delete ?":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Template Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[9]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div[2]/p[2]").text
    if txt == "Are you sure you want to delete ?":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on URL in DLT')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "url_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Add Short URL in DLT')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "create_url")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify add short url pop-up and add and cancel button')
def step_impl(context):
    time.sleep(2)
    add_button = context.driver.find_element(By.ID, "add_url")
    context.driver.execute_script("arguments[0].click();", add_button)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div/span/span").text
    if txt == "Please Enter URL":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on delete button of action and verify pop-up and close button')
def step_impl(context):
    time.sleep(2)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']"
                                                          "/div[2]/table/tbody/tr[2]/td[6]/a[2]/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div/div[2]/p[2]").text
    if txt == "Are you sure want to delete?":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    time.sleep(1)
    close_button = context.driver.find_element(By.ID, "delete_cancel")
    context.driver.execute_script("arguments[0].click();", close_button)


@then(u'Click on API')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_api']/p")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Generate API')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "idkey")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify generate API pop-up')
def step_impl(context):
    time.sleep(2)
    submit_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                          "div[1]/div[2]/div/div/div/div[3]/a[2]")
    context.driver.execute_script("arguments[0].click();", submit_button)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                "div[1]/div[2]/div/div/div/div[2]/div[1]/span/span").text
    if txt == "Account Type has not been created... contact seller":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                          "div[1]/div[2]/div/div/div/div[3]/a[1]")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Verify API Edit pop-up')
def step_impl(context):
    time.sleep(2)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='apiedit_2200']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Edit API Key Details":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                          "div[1]/div[2]/div/div/div/div[3]/a[1]")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Verify API Delete pop-up')
def step_impl(context):
    time.sleep(1)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                          "div[2]/table/tbody/tr[2]/td[9]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                "div[1]/div[2]/div/div/div/div[2]/div/p[2]").text
    if txt == "Are you sure want to delete API?":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                          "div[1]/div[2]/div/div/div/div[3]/a[1]")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Phonebook group Action tab click on edit button and verify pop-up')
def step_impl(context):
    time.sleep(2)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='groupedit_501']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/"
                                          "div[2]/div/div/div/div/div/div[2]/div[1]/input").clear()
    update_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                          "div[1]/div[2]/div/div/div/div/div/div[3]/input[2]")
    context.driver.execute_script("arguments[0].click();", update_button)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                "div[1]/div[2]/div/div/div/div/div/div[1]/p[1]").text
    if txt == "Edit Group":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']"
                                                          "/div[1]/div[2]/div/div/div/div/div/div[3]/input[1]")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Phonebook group Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(2)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='tab_content']/table/tbody/tr[2]/td[4]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/"
                                                "div[2]/div/div/div/div/div/div[2]/p").text
    if txt == "Phone Numbers Already present for this group : Test(501)":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    ok_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Verify add group in phonebook')
def step_impl(context):
    time.sleep(2)
    add_button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", add_button)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                "div[1]/div[2]/div/div/div/div/div/div[1]/p[1]").text
    if txt == "Add Group":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Phonebook contacts Action tab click on edit button and verify pop-up')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "group-select"))
    select.select_by_visible_text("Test(501)")
    search_button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", search_button)

    time.sleep(2)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='contactedit_7008427274']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    context.driver.find_element(By.XPATH, "//*[@id='addcontact']/div/div/div[2]/div[1]/div[1]/input").clear()
    update_button = context.driver.find_element(By.XPATH, "//*[@id='addcontact']/div/div/div[3]/input[2]")
    context.driver.execute_script("arguments[0].click();", update_button)
    txt = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]"
                                                "/div/div[2]/div/div/div/div[2]/div[1]/div[1]/span/span").text
    if txt == "Please Enter Contact Name":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.XPATH, "//*[@id='addcontact']/div/div/div[3]/input[1]")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Phonebook contacts Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "group-select"))
    select.select_by_visible_text("Test(501)")
    search_button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", search_button)

    time.sleep(2)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='contacts-table']/tbody/tr[2]/td[5]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)

    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div[2]/p[2]").text
    if txt == "Are you sure you want to delete?":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Verify add contacts pop-up')
def step_impl(context):
    time.sleep(2)
    add_button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", add_button)
    txt = context.driver.find_element(By.XPATH, "//*[@id='addcontact']/div/div/div[2]/span/span").text
    if txt == "Please Select any one opiton !!!":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Verify delete selected in contacts')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "delete-selected")
    context.driver.execute_script("arguments[0].click();", button)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    ok_button = context.driver.find_element(By.ID, "delete")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Verify delete all in contacts')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "group-select"))
    select.select_by_visible_text("Test(501)")
    search_button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", search_button)

    time.sleep(2)
    delete_button = context.driver.find_element(By.ID, "delete-phonebook-number")
    context.driver.execute_script("arguments[0].click();", delete_button)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div[2]/p[2]").text
    if txt == "Are you sure you want to delete ?":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(2)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Click on Blacklist Category')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "blacklist_cat_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Config blacklist category Action tab click on edit button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='blacklistedit_1301']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    context.driver.find_element(By.ID, "blacklist_desc").clear()
    time.sleep(1)

    update_button = context.driver.find_element(By.ID, "update_blacklist")
    context.driver.execute_script("arguments[0].click();", update_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                "div[1]/div[2]/div/div/div/div[2]/div[3]/span/span").text
    if txt == "Please Enter Description":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Config blacklist category Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='delete']/img")
    context.driver.execute_script("arguments[0].click();", delete_button)

    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    ok_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Click on Add Blacklist in blacklist category')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "add_blacklist")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify add blacklist pop-up in blacklist category')
def step_impl(context):
    time.sleep(1)
    add_button = context.driver.find_element(By.ID, "create_blacklist")
    context.driver.execute_script("arguments[0].click();", add_button)

    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                "div[1]/div[2]/div/div/div/div[2]/div[1]/span/span").text
    if txt == "Please Enter Name":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'verify delete selected in add blacklist number')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "delete-blacklist-number")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-add-blacklist-number']/div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'verify delete all in add blacklist number')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "delete-blacklist-number")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH,
                                      "//*[@id='pills-add-blacklist-number']/div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Config blacklist Number Action tab click on edit button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "black_category_table"))
    select.select_by_visible_text("Test[1301]")
    search_button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", search_button)

    time.sleep(1)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='blacklistedit_9556098190']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='tab_content']/div/div/div/div/div[1]/p").text
    if txt == "Edit blacklist Number":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Config blacklist Number Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "black_category_table"))
    select.select_by_visible_text("Test[1301]")
    search_button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", search_button)

    time.sleep(1)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='bw-number-table']/tbody/tr[2]/td[6]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-add-blacklist-number']/"
                                                "div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Caution":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Config blacklist Number Description tab click on description and verify pop-up')
def step_impl(context):
    time.sleep(2)
    desc_button = context.driver.find_element(By.XPATH, "//*[@id='bw-number-table']/tbody/tr[2]/td[4]/a/img")
    context.driver.execute_script("arguments[0].click();", desc_button)
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[1]/p[1]").text
    if txt == "Description":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    ok_button = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Config Whitelist category Action tab click on edit button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='whitelistedit_1302']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    context.driver.find_element(By.ID, "whitelist_name").clear()
    time.sleep(1)

    update_button = context.driver.find_element(By.ID, "update_whitelist")
    context.driver.execute_script("arguments[0].click();", update_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                "div[1]/div[2]/div/div/div/div[2]/div[1]/span/span").text
    if txt == "Please Enter Name":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Config Whitelist category Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='delete']/img")
    context.driver.execute_script("arguments[0].click();", delete_button)

    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    ok_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Click on Add Whitelist in Whitelist category')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "add_whitelist")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Add Whitelist pop-up in Whitelist category')
def step_impl(context):
    time.sleep(1)
    add_button = context.driver.find_element(By.ID, "create_whitelist")
    context.driver.execute_script("arguments[0].click();", add_button)

    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                "div[1]/div[2]/div/div/div/div[2]/div[1]/span/span").text
    if txt == "Please Enter Name":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'verify delete selected in add Whitelist number')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "delete-whitelist-number")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH,
                                      "//*[@id='pills-add-whitelist-number']/div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'verify delete all in add Whitelist number')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "delete-whitelist-number")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-add-whitelist-number']/"
                                                "div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Warning":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Config Whitelist Number Action tab click on edit button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "whitelist_category_id"))
    select.select_by_visible_text("Test[1302]")
    search_button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", search_button)

    time.sleep(1)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='whitelistedit_7008427274']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='tab_content']/div/div/div/div/div[1]/p").text
    if txt == "Edit whitelist Number":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel_modal")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Config Whitelist Number Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "whitelist_category_id"))
    select.select_by_visible_text("Test[1302]")
    search_button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", search_button)

    time.sleep(1)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='bw-number-table']/tbody/tr[2]/td[6]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='pills-add-whitelist-number']/"
                                                "div[2]/div/div/div/div[1]/p[1]").text
    if txt == "Caution":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Config Whitelist Number Description tab click on description and verify pop-up')
def step_impl(context):
    time.sleep(2)
    desc_button = context.driver.find_element(By.XPATH, "//*[@id='bw-number-table']/tbody/tr[2]/td[4]/a/img")
    context.driver.execute_script("arguments[0].click();", desc_button)
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[1]/p[1]").text
    if txt == "Description":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    ok_button = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Verify Content pop-up in Notification')
def step_impl(context):
    time.sleep(2)
    cont_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table[2]/tbody/tr[2]/td[2]/a/img")
    context.driver.execute_script("arguments[0].click();", cont_button)
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='bd-example-modal-lg']/div/div/div[1]/p[1]").text
    if txt == "Content":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    ok_button = context.driver.find_element(By.ID, "ok_modal")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'Verify Add Notification pop-up')
def step_impl(context):
    time.sleep(1)
    add_button = context.driver.find_element(By.ID, "add")
    context.driver.execute_script("arguments[0].click();", add_button)

    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[1]/span/span").text
    if txt == "Please Enter Subject":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Notification Action tab click on edit button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    edit_button = context.driver.find_element(By.XPATH, "//*[@id='idedit_54321']/img")
    context.driver.execute_script("arguments[0].click();", edit_button)
    time.sleep(1)
    txt = context.driver.find_element(By.XPATH, "//*[@id='notification_title']").text
    if txt == "Edit Notification":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)


@then(u'Notification Action tab click on delete button and verify pop-up')
def step_impl(context):
    time.sleep(1)
    delete_button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/"
                                                          "div[2]/table[2]/tbody/tr[2]/td[5]/a/img")
    context.driver.execute_script("arguments[0].click();", delete_button)
    time.sleep(1)
    txt = context.driver.find_element(By.ID, "notification_title").text
    if txt == "Caution":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
    time.sleep(1)
    cancel_button = context.driver.find_element(By.ID, "cancel")
    context.driver.execute_script("arguments[0].click();", cancel_button)

