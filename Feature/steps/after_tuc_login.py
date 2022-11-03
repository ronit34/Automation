from behave import *
from selenium.webdriver.common.by import By

import time

after_tuc_login_id_list = []
after_tuc_login_id_list.append('menu_dashboard')
after_tuc_login_id_list.append('menu_campaign')
after_tuc_login_id_list.append('menu_users')
after_tuc_login_id_list.append('menu_credit_allocation')
after_tuc_login_id_list.append('menu_report')
after_tuc_login_id_list.append('menu_manage')
after_tuc_login_id_list.append('menu_smpps_view')
after_tuc_login_id_list.append('menu_api')
after_tuc_login_id_list.append('menu_phonebook')
after_tuc_login_id_list.append('dropdown-caret')
after_tuc_login_id_list.append('dropdown-caret')




@then(u'Check element are present')
def step_impl(context):
    for element_id in after_tuc_login_id_list:
        try:
            context.driver.implicitly_wait(20)
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
            # print(*element_id, sep=" is present\n")
        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()
