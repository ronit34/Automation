from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import CommonUtility as CU

# english short
DLT_templateIDEshortObj = CU.DLT_templateIDEshort()
DLT_templateIDEshort_dropdownobj=CU.DLT_templateIDEshort_dropdown()

# Promo english 1 var
DLT_templateIDEshortPromoObj = CU.DLT_templateIDEshort_Promo()
DLT_templateIDEshort_Promo_dropdownobj=CU.DLT_templateIDEshort_Promo_dropdown()

#Hindhi short
DLT_templateID1Obj = CU.DLT_templateID1()
DLT_templateID_dropdown11obj=CU.DLT_templateID_dropdown11()


#hindhi long
DLT_templateID2Obj = CU.DLT_templateID2()
DLT_templateID_dropdown22obj=CU.DLT_templateID_dropdown22()

#Dynamic one var
DLT_templateID3Obj = CU.DLT_templateID3()
DLT_templateID_dropdown33obj=CU.DLT_templateID_dropdown33()

#Dynamic Three var
DLT_templateID4Obj = CU.DLT_templateID4()
DLT_templateID_dropdown44obj=CU.DLT_templateID_dropdown44()

#Dynamic Hindi One var
DLT_templateID5Obj = CU.DLT_templateID5()
DLT_templateID_dropdown55obj=CU.DLT_templateID_dropdown55()

#Dynamic Hindi One var
DLT_templateID6Obj = CU.DLT_templateID6()
DLT_templateID_dropdown66obj=CU.DLT_templateID_dropdown66()

# Promo hindi short 1 var
DLT_templateIDPromoObj = CU.DLT_templateIDPromo()
DLT_templateID_Promo_dropdownobj=CU.DLT_templateID_Promo_dropdown()

@then(u'create multiple template')
def step_impl(context):
    i=1
    while(i<2):
        #***********************English Short************************************************
        if(context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[2]").is_displayed()):
            button = context.driver.find_element(By.ID, "create_template")
            context.driver.execute_script("arguments[0].click();", button)
            for element_id in DLT_templateIDEshortObj.DLT_templateIDEshort_inputbox_list.keys():
                context.driver.find_element(By.ID, element_id).send_keys(
                    DLT_templateIDEshortObj.DLT_templateIDEshort_inputbox_list[element_id])
                print(f"{element_id}")

            for element_id in DLT_templateIDEshort_dropdownobj.DLT_templateIDEshort_dropdown_list.keys():
                try:
                    context.driver.implicitly_wait(20)
                    element_obj = context.driver.find_element(By.ID, element_id)
                    context.driver.implicitly_wait(20)
                    select = Select(element_obj)
                    context.driver.implicitly_wait(20)
                    select.select_by_visible_text(
                        DLT_templateIDEshort_dropdownobj.DLT_templateIDEshort_dropdown_list[element_id])

                except NameError:
                    print(NameError)

            time.sleep(2)
            entity = context.driver.find_element(By.ID, "template_sender_id")
            select = Select(entity)
            select.select_by_visible_text("123456")

            context.driver.find_element(By.ID, "add_template").click()
            time.sleep(1)

#  ---------------------------------->>  english short promo template < ----------------------------------

        if (context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[2]").is_displayed()):
            button = context.driver.find_element(By.ID, "create_template")
            context.driver.execute_script("arguments[0].click();", button)
            for element_id in DLT_templateIDEshortPromoObj.DLT_templateIDEshort_Promo_inputbox_list.keys():
                context.driver.find_element(By.ID, element_id).send_keys(
                    DLT_templateIDEshortPromoObj.DLT_templateIDEshort_Promo_inputbox_list[element_id])
                print(f"{element_id}")

            for element_id in DLT_templateIDEshort_Promo_dropdownobj.DLT_templateIDEshort_Promo_dropdown_list.keys():
                try:
                    context.driver.implicitly_wait(20)
                    element_obj = context.driver.find_element(By.ID, element_id)
                    context.driver.implicitly_wait(20)
                    select = Select(element_obj)
                    context.driver.implicitly_wait(20)
                    select.select_by_visible_text(
                        DLT_templateIDEshort_Promo_dropdownobj.DLT_templateIDEshort_Promo_dropdown_list[element_id])

                except NameError:
                    print(NameError)

            time.sleep(2)
            entity = context.driver.find_element(By.ID, "template_sender_id")
            select = Select(entity)
            select.select_by_visible_text("123456")

            context.driver.find_element(By.ID, "add_template").click()
            time.sleep(1)


#  ---------------------------->>>>                         <<<<---------------------------------------

        if(context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[3]").is_displayed()):
            button = context.driver.find_element(By.ID, "create_template")
            context.driver.execute_script("arguments[0].click();", button)
            for element_id in DLT_templateID1Obj.DLT_templateID1_inputbox_list.keys():
                context.driver.find_element(By.ID, element_id).send_keys(
                    DLT_templateID1Obj.DLT_templateID1_inputbox_list[element_id])
                print(f"{element_id}")

            for element_id in DLT_templateID_dropdown11obj.DLT_templateID_dropdown11_inputbox_list.keys():
                try:
                    context.driver.implicitly_wait(20)
                    element_obj = context.driver.find_element(By.ID, element_id)
                    context.driver.implicitly_wait(20)
                    select = Select(element_obj)
                    context.driver.implicitly_wait(20)
                    select.select_by_visible_text(
                        DLT_templateID_dropdown11obj.DLT_templateID_dropdown11_inputbox_list[element_id])

                except NameError:
                    print(NameError)

            time.sleep(2)
            entity = context.driver.find_element(By.ID, "template_sender_id")
            select = Select(entity)
            select.select_by_visible_text("123456")

            time.sleep(1)
            button = context.driver.find_element(By.ID,"add_template")
            context.driver.execute_script("arguments[0].click();", button)

            time.sleep(1)
        if(context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[4]").is_displayed()):

            button = context.driver.find_element(By.ID, "create_template")
            context.driver.execute_script("arguments[0].click();", button)
            for element_id in DLT_templateID2Obj.DLT_templateID2_inputbox_list.keys():
                context.driver.find_element(By.ID, element_id).send_keys(
                    DLT_templateID2Obj.DLT_templateID2_inputbox_list[element_id])
                print(f"{element_id}")

            for element_id in DLT_templateID_dropdown22obj.DLT_templateID_dropdown22_inputbox_list.keys():
                try:
                    context.driver.implicitly_wait(20)
                    element_obj = context.driver.find_element(By.ID, element_id)
                    context.driver.implicitly_wait(20)
                    select = Select(element_obj)
                    context.driver.implicitly_wait(20)
                    select.select_by_visible_text(
                        DLT_templateID_dropdown22obj.DLT_templateID_dropdown22_inputbox_list[element_id])

                except NameError:
                    print(NameError)

            time.sleep(2)
            entity = context.driver.find_element(By.ID, "template_sender_id")
            select = Select(entity)
            select.select_by_visible_text("123456")

            context.driver.find_element(By.ID, "add_template").click()
            time.sleep(1)

            #******************** Dynamic 1var ***********************************

            if (context.driver.find_element(By.XPATH, "// *[ @ id = 'template_table'] / tbody / tr[5] / td[2]").is_displayed()):

                button = context.driver.find_element(By.ID, "create_template")
                context.driver.execute_script("arguments[0].click();", button)
                for element_id in DLT_templateID3Obj.DLT_templateID3_inputbox_list.keys():
                    context.driver.find_element(By.ID, element_id).send_keys(
                        DLT_templateID3Obj.DLT_templateID3_inputbox_list[element_id])
                    print(f"{element_id}")

                for element_id in DLT_templateID_dropdown33obj.DLT_templateID_dropdown33_inputbox_list.keys():
                    try:
                        context.driver.implicitly_wait(20)
                        element_obj = context.driver.find_element(By.ID, element_id)
                        context.driver.implicitly_wait(20)
                        select = Select(element_obj)
                        context.driver.implicitly_wait(20)
                        select.select_by_visible_text(
                            DLT_templateID_dropdown33obj.DLT_templateID_dropdown33_inputbox_list[element_id])

                    except NameError:
                        print(NameError)

                time.sleep(2)
                entity = context.driver.find_element(By.ID, "template_sender_id")
                select = Select(entity)
                select.select_by_visible_text("123456")

                context.driver.find_element(By.ID, "add_template").click()
                time.sleep(1)
                # ******************** Dynamic 3var ***********************************

                if (context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[2]").is_displayed()):

                    button = context.driver.find_element(By.ID, "create_template")
                    context.driver.execute_script("arguments[0].click();", button)
                    for element_id in DLT_templateID4Obj.DLT_templateID4_inputbox_list.keys():
                        context.driver.find_element(By.ID, element_id).send_keys(
                            DLT_templateID4Obj.DLT_templateID4_inputbox_list[element_id])
                        print(f"{element_id}")

                    for element_id in DLT_templateID_dropdown44obj.DLT_templateID_dropdown44_inputbox_list.keys():
                        try:
                            context.driver.implicitly_wait(20)
                            element_obj = context.driver.find_element(By.ID, element_id)
                            context.driver.implicitly_wait(20)
                            select = Select(element_obj)
                            context.driver.implicitly_wait(20)
                            select.select_by_visible_text(
                                DLT_templateID_dropdown44obj.DLT_templateID_dropdown44_inputbox_list[element_id])

                        except NameError:
                            print(NameError)

                    time.sleep(2)
                    entity = context.driver.find_element(By.ID, "template_sender_id")
                    select = Select(entity)
                    select.select_by_visible_text("123456")

                    context.driver.find_element(By.ID, "add_template").click()
                    time.sleep(1)

                    ####################################   dynaminc long 3 variable ##################


                if (context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[2]/td[2]").is_displayed()):

                    button = context.driver.find_element(By.ID, "create_template")
                    context.driver.execute_script("arguments[0].click();", button)
                    for element_id in DLT_templateID6Obj.DLT_templateID6_inputbox_list.keys():
                        context.driver.find_element(By.ID, element_id).send_keys(
                            DLT_templateID6Obj.DLT_templateID6_inputbox_list[element_id])
                        print(f"{element_id}")

                    for element_id in DLT_templateID_dropdown66obj.DLT_templateID_dropdown66_inputbox_list.keys():
                        try:
                            context.driver.implicitly_wait(20)
                            element_obj = context.driver.find_element(By.ID, element_id)
                            context.driver.implicitly_wait(20)
                            select = Select(element_obj)
                            context.driver.implicitly_wait(20)
                            select.select_by_visible_text(
                                DLT_templateID_dropdown66obj.DLT_templateID_dropdown66_inputbox_list[element_id])

                        except NameError:
                            print(NameError)

                    time.sleep(2)
                    entity = context.driver.find_element(By.ID, "template_sender_id")
                    select = Select(entity)
                    select.select_by_visible_text("123456")

                    context.driver.find_element(By.ID, "add_template").click()
                    time.sleep(1)
                #************Dynamic Hindi One Var***************

                if (context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[7]").is_displayed()):

                    button = context.driver.find_element(By.ID, "create_template")
                    context.driver.execute_script("arguments[0].click();", button)
                    for element_id in DLT_templateID5Obj.DLT_templateID5_inputbox_list.keys():
                        context.driver.find_element(By.ID, element_id).send_keys(
                            DLT_templateID5Obj.DLT_templateID5_inputbox_list[element_id])
                        print(f"{element_id}")

                    for element_id in DLT_templateID_dropdown55obj.DLT_templateID_dropdown55_inputbox_list.keys():
                        try:
                            context.driver.implicitly_wait(20)
                            element_obj = context.driver.find_element(By.ID, element_id)
                            context.driver.implicitly_wait(20)
                            select = Select(element_obj)
                            context.driver.implicitly_wait(20)
                            select.select_by_visible_text(
                                DLT_templateID_dropdown55obj.DLT_templateID_dropdown55_inputbox_list[element_id])

                        except NameError:
                            print(NameError)

                    time.sleep(2)
                    entity = context.driver.find_element(By.ID, "template_sender_id")
                    select = Select(entity)
                    select.select_by_visible_text("123456")

                    context.driver.find_element(By.ID, "add_template").click()
                    time.sleep(1)

                if (context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[7]").is_displayed()):

                    button = context.driver.find_element(By.ID, "create_template")
                    context.driver.execute_script("arguments[0].click();", button)
                    for element_id in DLT_templateIDPromoObj.DLT_templateIDPromo_inputbox_list.keys():
                        context.driver.find_element(By.ID, element_id).send_keys(
                            DLT_templateIDPromoObj.DLT_templateIDPromo_inputbox_list[element_id])
                        print(f"{element_id}")

                    for element_id in DLT_templateID_Promo_dropdownobj.DLT_templateID_Promo_dropdown_inputbox_list.keys():
                        try:
                            context.driver.implicitly_wait(20)
                            element_obj = context.driver.find_element(By.ID, element_id)
                            context.driver.implicitly_wait(20)
                            select = Select(element_obj)
                            context.driver.implicitly_wait(20)
                            select.select_by_visible_text(
                                DLT_templateID_Promo_dropdownobj.DLT_templateID_Promo_dropdown_inputbox_list[element_id])

                        except NameError:
                            print(NameError)

                    time.sleep(2)
                    entity = context.driver.find_element(By.ID, "template_sender_id")
                    select = Select(entity)
                    select.select_by_visible_text("123456")

                    context.driver.find_element(By.ID, "add_template").click()
                    time.sleep(1)

            i=i+1

    # time.sleep(2)
    # context.driver.close()