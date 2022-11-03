from datetime import datetime
import calendar

x = datetime.now()
current_Day_Date = (x.strftime("%A" " " "%d" " " "%B" " " "%Y"))


class master_update_credit_balance:
    master_update_credit_balance_list = {}
    master_update_credit_balance_list['available_credits'] = "0"
    master_update_credit_balance_list['current_date'] = current_Day_Date


# *****************Master Balance****************************
class master_balance:
    master_balance_inputbox_list = {}
    master_balance_inputbox_list['current_balance'] = "Current Balance = 0"
    master_balance_inputbox_list['update_balance'] = "+Update Balance"
    master_balance_inputbox_list['title'] = "Master Balance"
    master_balance_inputbox_list['current_date'] = current_Day_Date
    master_balance_inputbox_list['bell_icon'] = "Bell Icon"


# *****************Master Update Balance****************************
class Master_Update_Balance:
    Master_Update_Balance_inputbox_list = {}
    # Master_Update_Balance_inputbox_list['balance_title'] = "Update Balance"
    # Master_Update_Balance_inputbox_list['cancel'] = "button"
    # Master_Update_Balance_inputbox_list['balance_subtitle'] = "Update balance by entering amount below"
    # Master_Update_Balance_inputbox_list['amount'] = "amount"
    # Master_Update_Balance_inputbox_list['currency'] = "rupees"
    # Master_Update_Balance_inputbox_list['add'] = "Add"
    # Master_Update_Balance_inputbox_list['cancel'] = "Cancel"
    Master_Update_Balance_inputbox_list[
        "//*[@id='balance_title']"] = "Update Credits"  ##### Balance is replaced with credits #####
    Master_Update_Balance_inputbox_list["//*[@id='balance_subtitle']"] = "Update Credits by entering amount below"
    Master_Update_Balance_inputbox_list["//*[@id='myModal']/div/div/div[2]/div/label"] = "Credits"
    Master_Update_Balance_inputbox_list["//*[@id='amount']"] = "Enter Credits"
    Master_Update_Balance_inputbox_list["//*[@id='add']"] = "Add"
    Master_Update_Balance_inputbox_list["//*[@id='cancel']"] = "Cancel"


class Master_Update_Balance_label:
    Master_Update_Balance_label_inputbox_list = {}
    # Master_Update_Balance_label_inputbox_list['balance_title'] = "Update Balance"
    # Master_Update_Balance_label_inputbox_list['balance_subtitle'] = "Update balance by entering amount below"
    # Master_Update_Balance_label_inputbox_list['currency'] = "rupees"
    # Master_Update_Balance_label_inputbox_list['add'] = "Add"
    Master_Update_Balance_label_inputbox_list[
        "//*[@id='balance_title']"] = "Update Credits"  ##### Balance is replaced with credits #####
    Master_Update_Balance_label_inputbox_list["//*[@id='balance_subtitle']"] = "Update Credits by entering amount below"
    Master_Update_Balance_label_inputbox_list["//*[@id='myModal']/div/div/div[2]/div/label"] = "Credits"
    Master_Update_Balance_label_inputbox_list["//*[@id='add']"] = "Add"


# ******************************* Master License ***********************************************

class master_license:
    master_license_inputbox_list = {}
    master_license_inputbox_list['current_date'] = current_Day_Date
    master_license_inputbox_list['update_childtuc_license'] = "Button"
    master_license_inputbox_list['update_smpps_license'] = "Button"
    master_license_inputbox_list['update_smsapi_license'] = "Button"
    master_license_inputbox_list['available_credits'] = 90000


class master_license_CTUC:
    master_license_CTUC_inputbox_list = {}
    master_license_CTUC_inputbox_list['value'] = "text"
    master_license_CTUC_inputbox_list['add'] = "Button"
    master_license_CTUC_inputbox_list['cancel'] = "Button"
    master_license_CTUC_inputbox_list['value'] = "1100"


# class master_license_SMPPS:
#     master_license_SMPPS_inputbox_list = {}
#     master_license_SMPPS_inputbox_list['value'] ="text"
#     master_license_SMPPS_inputbox_list['add'] = "Button"
#     master_license_SMPPS_inputbox_list['cancel'] = "Button"
#     master_license_SMPPS_inputbox_list['value'] = "1100"


# *********************************Credit Allocation**************************************************
class credit_allocation:
    credit_allocation_inputbox_list = {}
    credit_allocation_inputbox_list['current_date'] = current_Day_Date
    credit_allocation_inputbox_list['available_credits'] = ""
    credit_allocation_inputbox_list['pills-user-alloc'] = "Userwise Allocation"
    credit_allocation_inputbox_list['pills-all-alloc'] = "All Allocation"
    credit_allocation_inputbox_list['searchTuc'] = "search box"
    credit_allocation_inputbox_list['usr-alloc-search'] = "Search"
    credit_allocation_inputbox_list['update_credit'] = "Update Credit"


class credit_allocation_label:
    credit_allocation_label_inputbox_list = {}
    credit_allocation_label_inputbox_list['current_date'] = current_Day_Date
    # credit_allocation_label_inputbox_list['available_credits'] = ""
    credit_allocation_label_inputbox_list['pills-user-alloc'] = "Userwise Allocation"
    credit_allocation_label_inputbox_list['pills-all-alloc'] = "All Allocation"
    # credit_allocation_label_inputbox_list['tuc_list'] = ""
    credit_allocation_label_inputbox_list['usr-alloc-search'] = "Search"
    credit_allocation_label_inputbox_list['update_credit'] = "Update Credit"


# *********************************Credit ADD **********************************
class credit_add:
    credit_add_inputbox_list = {}
    credit_add_inputbox_list['available_credits'] = 100000
    credit_add_inputbox_list['select_tuc'] = ""
    # credit_add_inputbox_list['wfid_temp92163'] = "Add-Credits"
    # credit_add_inputbox_list['wfid_temp92227'] = "Deduct-Credits"
    # credit_add_inputbox_list['credits_amount'] = "Enter Amount"
    credit_add_inputbox_list['credits_amount'] = "Enter Credits"
    # credit_add_inputbox_list['select_currency'] = "Search"
    credit_add_inputbox_list['cancel_modal'] = "Cancel"
    credit_add_inputbox_list['update_credits'] = "Update"


class credit_add_label:
    credit_add_label_inputbox_list = {}
    credit_add_label_inputbox_list['available_credits'] = "100000"
    credit_add_label_inputbox_list['select_tuc'] = ""
    # credit_add_label_inputbox_list['credits_amount'] = "Enter Amount"
    credit_add_label_inputbox_list['credits_amount'] = "Enter Credits"
    # credit_add_label_inputbox_list['select_currency'] = "Search"
    credit_add_label_inputbox_list['cancel_modal'] = "Cancel"
    credit_add_label_inputbox_list['update_credits'] = "Update"


# *********************Tenant Creator**************************************************
class tenant_creator:
    tenant_creator_inputbox_list = {}
    tenant_creator_inputbox_list['name'] = "Onexmedia"
    tenant_creator_inputbox_list['description'] = "Its a bank"
    tenant_creator_inputbox_list['childtuc'] = "500"
    tenant_creator_inputbox_list['smpps'] = "500"
    tenant_creator_inputbox_list['smsapi'] = "500"
    # tenant_creator_inputbox_list['smsapi_tenant'] = "8"
    tenant_creator_inputbox_list['cancel'] = "Button"
    tenant_creator_inputbox_list['save_tenant'] = "Button"
    tenant_creator_inputbox_list['save_tenant'] = "Button"


class user_creator:
    user_creator_inputbox_list = {}
    user_creator_inputbox_list['username'] = "Onexadmin"
    user_creator_inputbox_list['password'] = "ali"
    user_creator_inputbox_list['fname'] = "Onex"
    user_creator_inputbox_list['lname'] = "Admin"
    user_creator_inputbox_list['email'] = "onex@"
    user_creator_inputbox_list['mob_no'] = "8"
    user_creator_inputbox_list['comp_name'] = "OneXtel"
    user_creator_inputbox_list['web'] = "onextel.tech"
    user_creator_inputbox_list['other_mob_no'] = "3"
    user_creator_inputbox_list['cancel'] = "Button"
    user_creator_inputbox_list['save_user'] = "Button"
    user_creator_inputbox_list['save_user'] = "Button"


# ************************ Tenant User Management *************************

class User_Mgmt_search:
    User_Mgmt_search_list = {}
    User_Mgmt_search_list["/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div"] = "No Record found"


# ************************* Code For Dropdown **********************************
class user_creator_dropdown:
    user_creator_dropdown_inputbox_list = {}
    user_creator_dropdown_inputbox_list['role_type'] = "Tenant Admin"
    user_creator_dropdown_inputbox_list['tenant'] = "Onexmedia"


# ********************** TUC Creator *******************************************
class tucinfo_id:
    tucinfo_id_list = {}
    # tucinfo_id_list['cost_per_otp'] = "10"    ##### Wallet System Updated
    # tucinfo_id_list['cost_per_tx'] = "60"
    # tucinfo_id_list['cost_per_promo'] = "30"
    # tucinfo_id_list['cost_per_simroute'] = "40"
    # tucinfo_id_list['scrubbing_cost'] = "40"

    tucinfo_id_list['name'] = "ICICI"
    tucinfo_id_list['otp_acc_type'] = "On Delivery"  #### Updated fields
    tucinfo_id_list['trans_acc_type'] = "On Delivery"
    tucinfo_id_list['promo_acc_type'] = "On Delivery"
    tucinfo_id_list['gov_acc_type'] = "On Delivery"
    tucinfo_id_list['sim_acc_type'] = "On Delivery"
    tucinfo_id_list['default_acc_type'] = "On Delivery"

    # tucinfo_id_list['cost_unit'] = "paisa"
    # tucinfo_id_list['accmgr'] = "sant"
    # tucinfo_id_list['billing_type'] = "POSTPAID"
    # tucinfo_id_list['dlt_charges'] = "On Delivery"
    # tucinfo_id_list['sms_charges'] = "On Delivery"
    tucinfo_id_list['mask_phone'] = "Yes"
    tucinfo_id_list['validity'] = "101"
    # tucinfo_id_list['onex_gatewaypanel1'] = "checkbox"
    tucinfo_id_list['childtuc'] = "100"
    tucinfo_id_list['smpps'] = "100"
    tucinfo_id_list['smsapi'] = "100"
    tucinfo_id_list['cancel'] = " Cancel Button"
    tucinfo_id_list['save_tuc'] = " Create Button"
    tucinfo_id_list['save_tuc'] = " Create Button"


class tucinfo_of_telspiel:
    tucinfo_id_of_telspiel_list = {}

    tucinfo_id_of_telspiel_list['name'] = "TESTRKP"
    tucinfo_id_of_telspiel_list['otp_acc_type'] = "On Delivery"
    tucinfo_id_of_telspiel_list['trans_acc_type'] = "On Delivery"
    tucinfo_id_of_telspiel_list['promo_acc_type'] = "On Delivery"
    tucinfo_id_of_telspiel_list['gov_acc_type'] = "On Delivery"
    tucinfo_id_of_telspiel_list['sim_acc_type'] = "On Delivery"
    tucinfo_id_of_telspiel_list['default_acc_type'] = "On Delivery"
    tucinfo_id_of_telspiel_list['billing_type'] = "PREPAID"
    tucinfo_id_of_telspiel_list['mask_phone'] = "Yes"
    tucinfo_id_of_telspiel_list['validity'] = "101"
    tucinfo_id_of_telspiel_list['childtuc'] = "99"
    tucinfo_id_of_telspiel_list['smpps'] = "100"
    tucinfo_id_of_telspiel_list['smsapi'] = "100"
    # tucinfo_id_of_telspiel_list['cancel'] = " Cancel Button"
    tucinfo_id_of_telspiel_list['save_tuc'] = " Create Button"
    # tucinfo_id_of_telspiel_list['save_tuc'] = " Create Button"


# *****************************Check TUC is Delete or not******************
class tuc_delete:
    tuc_delete_list = {}
    tuc_delete_list[
        "//*[@id='pills-campaign']/div[2]/div/div/div/div/div[2]/p"] = "This account cannot be deleted because it has unused credit balance of 500"
    tuc_delete_list["//*[@id='pills-campaign']/div[2]/div/div/div/div/div[3]/a"] = "close"


# ****************************TUC USER*******************************************
class tucuser_id:
    tucuser_id_list = {}
    tucuser_id_list['username'] = "ICICIAdmin"
    tucuser_id_list['password'] = "ali"
    tucuser_id_list['fname'] = "ICICI"
    tucuser_id_list['lname'] = "Admin"
    tucuser_id_list['email'] = "jaff@gmail.com"
    tucuser_id_list['mob_no'] = "1234567890"
    tucuser_id_list['comp_name'] = "onextel"
    tucuser_id_list['web'] = "Onextel.tech"
    tucuser_id_list['other_mob_no'] = "1234567899"
    tucuser_id_list['role_type'] = "Tuc Admin"
    tucuser_id_list['cancel'] = "Button"
    tucuser_id_list['tuc'] = "Button"
    tucuser_id_list['save_user'] = "Button"
    tucuser_id_list['save_user'] = "Button"


class tuc_default_gateway_dropdown_edit:
    tuc_default_gateway_dropdown_edit_list = {}
    # tuc_default_gateway_dropdown_edit_list['otp_gw'] = "AIRTEL-OTP-1"
    # tuc_default_gateway_dropdown_edit_list['promo_gw'] = "AIRTEL-OTP-1"
    # tuc_default_gateway_dropdown_edit_list['serv_imp_gw'] = "AIRTEL-OTP-1"
    # tuc_default_gateway_dropdown_edit_list['serv_exp_gw'] = "AIRTEL-OTP-1"
    # tuc_default_gateway_dropdown_edit_list['transpromo_gw'] = "AIRTEL-OTP-1"
    # tuc_default_gateway_dropdown_edit_list['govt_gw'] = "AIRTEL-OTP-1"
    # tuc_default_gateway_dropdown_edit_list['simroute_gw'] = "AIRTEL-OTP-1"
    tuc_default_gateway_dropdown_edit_list['otp_gw'] = "Dummy"
    tuc_default_gateway_dropdown_edit_list['promo_gw'] = "Dummy"
    tuc_default_gateway_dropdown_edit_list['serv_imp_gw'] = "Dummy"
    tuc_default_gateway_dropdown_edit_list['serv_exp_gw'] = "Dummy"
    tuc_default_gateway_dropdown_edit_list['transpromo_gw'] = "Dummy"
    tuc_default_gateway_dropdown_edit_list['govt_gw'] = "Dummy"
    tuc_default_gateway_dropdown_edit_list['simroute_gw'] = "Dummy"


# **************************** TUC HDFC*********************************************
class tuc_hdfc:
    tuc_hdfc_list = {}
    # tuc_hdfc_list['cost_per_otp'] = "10"                      ######## Wallet Updated
    # tuc_hdfc_list['cost_per_tx'] = "60"
    # tuc_hdfc_list['cost_per_promo'] = "30"
    # tuc_hdfc_list['cost_per_simroute'] = "40"
    # tuc_hdfc_list['scrubbing_cost'] = "40"

    tuc_hdfc_list['name'] = "HDFC"
    tuc_hdfc_list['otp_acc_type'] = "On Delivery"  #### Updated fields
    tuc_hdfc_list['trans_acc_type'] = "On Delivery"
    tuc_hdfc_list['promo_acc_type'] = "On Delivery"
    tuc_hdfc_list['gov_acc_type'] = "On Delivery"
    tuc_hdfc_list['sim_acc_type'] = "On Delivery"
    tuc_hdfc_list['default_acc_type'] = "On Delivery"

    # tuc_hdfc_list['cost_unit'] = "paisa"
    # tuc_hdfc_list['accmgr'] = "sant"
    tuc_hdfc_list['billing_type'] = "POSTPAID"
    # tuc_hdfc_list['dlt_charges'] = "On Delivery"
    # tuc_hdfc_list['sms_charges'] = "On Delivery"
    tuc_hdfc_list['mask_phone'] = "Yes"
    tuc_hdfc_list['validity'] = "101"
    # tuc_hdfc_list['onex_gatewaypanel1'] = "checkbox"
    tuc_hdfc_list['childtuc'] = "10"
    tuc_hdfc_list['smpps'] = "10"
    tuc_hdfc_list['smsapi'] = "10"
    tuc_hdfc_list['cancel'] = " Cancel Button"
    tuc_hdfc_list['save_tuc'] = " Create Button"
    tuc_hdfc_list['save_tuc'] = " Create Button"


class tuc_hdfc_user:
    tuc_hdfc_user_list = {}
    tuc_hdfc_user_list['username'] = "HDFCAdmin"
    tuc_hdfc_user_list['password'] = "ali"
    tuc_hdfc_user_list['fname'] = "HDFC"
    tuc_hdfc_user_list['lname'] = "Admin"
    tuc_hdfc_user_list['email'] = "jaff@gmail.com"
    tuc_hdfc_user_list['mob_no'] = "1234567890"
    tuc_hdfc_user_list['comp_name'] = "onextel"
    tuc_hdfc_user_list['web'] = "Onextel.tech"
    tuc_hdfc_user_list['other_mob_no'] = "1234567899"
    tuc_hdfc_user_list['role_type'] = "Tuc Admin"
    tuc_hdfc_user_list['cancel'] = "Button"
    tuc_hdfc_user_list['tuc'] = "Button"
    tuc_hdfc_user_list['save_user'] = "Button"
    tuc_hdfc_user_list['save_user'] = "Button"


# ***************************TUC CHILD LOGIN 1)CAMPAIGN **************************
class campaign:
    campaign_inputbox_list = {}
    campaign_inputbox_list['available_credits'] = "0"
    campaign_inputbox_list['current_date'] = current_Day_Date
    campaign_inputbox_list['create_campaign'] = ""


class campaign_add:
    campaign_add_inputbox_list = {}
    campaign_add_inputbox_list['campaign_name'] = "Enter Campaign Name"
    campaign_add_inputbox_list['campaign_desc'] = "Enter Description"
    campaign_add_inputbox_list['add_campaign'] = "Add"
    campaign_add_inputbox_list['cancel_modal'] = "Cancel"
    campaign_add_inputbox_list['close_modal'] = ""
    campaign_add_inputbox_list['close_modal'] = "button"


class campaign_add_button:
    campaign_add_button_inputbox_list = {}
    campaign_add_button_inputbox_list['available_credits'] = "0"
    campaign_add_button_inputbox_list['current_date'] = current_Day_Date
    campaign_add_button_inputbox_list['create_campaign'] = ""


# ***************************  Manage  *************************************

class DLT:
    DLT_inputbox_list = {}
    DLT_inputbox_list['available_credits'] = "0"
    DLT_inputbox_list['entityid_tab'] = "Entity IDs"
    DLT_inputbox_list['senderid_tab'] = "Sender IDs"
    DLT_inputbox_list['template_tab'] = "Template"
    DLT_inputbox_list['current_date'] = current_Day_Date
    # DLT_inputbox_list['url_tab'] = "URL"
    # DLT_inputbox_list['domain_tab'] = "Domain"
    # DLT_inputbox_list['signature_tab'] = "Signature"
    DLT_inputbox_list['create_entityid'] = "+ Add Entity Id"


class DLT_entityID:
    DLT_entityID_inputbox_list = {}
    DLT_entityID_inputbox_list['close_modal'] = "button"
    DLT_entityID_inputbox_list['entity_id'] = "123"
    DLT_entityID_inputbox_list['entity_name'] = "Onextel"
    DLT_entityID_inputbox_list['add_entityid'] = "add"
    DLT_entityID_inputbox_list['cancel_modal'] = "cancel"

    #################### more than 3 digits for masking check ################


class DLT_entityID_masked:
    DLT_entityID_masked_inputbox_list = {}
    DLT_entityID_masked_inputbox_list['close_modal'] = "button"
    DLT_entityID_masked_inputbox_list['entity_id'] = "123456"
    DLT_entityID_masked_inputbox_list['entity_name'] = "OneTech"
    DLT_entityID_masked_inputbox_list['add_entityid'] = "add"
    DLT_entityID_masked_inputbox_list['cancel_modal'] = "cancel"
    ##########################################################################


class DLT_senderID:
    DLT_senderID_inputbox_list = {}
    DLT_senderID_inputbox_list['close_modal'] = "close"
    DLT_senderID_inputbox_list['sender_name'] = "Enter ID"
    DLT_senderID_inputbox_list['sender_entity_id'] = "Select Entity Name"
    DLT_senderID_inputbox_list['add_sender_id'] = "Add"
    DLT_senderID_inputbox_list['cancel_modal'] = "Cancel"


class DLT_templateID:
    DLT_templateID_inputbox_list = {}
    DLT_templateID_inputbox_list['template_name'] = "English Long"
    DLT_templateID_inputbox_list['template_id'] = "12345"
    DLT_templateID_inputbox_list['template_description'] = "It is a template"
    DLT_templateID_inputbox_list[
        'template_content'] = "Message Writing is one of the common formal types of writing that we learn in our school curriculum {#var#} . A message can be simply described as certain information we need to give to a person when we can't directly communicate or contact them. The format of a message mainly comprises elements like date, time, receiver's name, the message and then the sender's name. This blog brings you all the details about message writing format, practice questions and more!"
    DLT_templateID_inputbox_list['cancel_modal'] = "Button"
    DLT_templateID_inputbox_list['add_template'] = "Button"
    DLT_templateID_inputbox_list['close_modal'] = "Button"

    ####################  Executed Campaign ########################################


class DLT_templateID_executed:
    DLT_templateID_executed_inputbox_list = {}
    DLT_templateID_executed_inputbox_list['template_name'] = "executed campaign"
    DLT_templateID_executed_inputbox_list['template_id'] = "12345"
    DLT_templateID_executed_inputbox_list['template_description'] = "It is a template"
    DLT_templateID_executed_inputbox_list[
        'template_content'] = "Message Writing is one of the common. "
    DLT_templateID_executed_inputbox_list['cancel_modal'] = "Button"
    DLT_templateID_executed_inputbox_list['add_template'] = "Button"
    DLT_templateID_executed_inputbox_list['close_modal'] = "Button"


#########################################################################################

class DLT_templateID_dropdown:
    DLT_templateID_dropdown_inputbox_list = {}
    DLT_templateID_dropdown_inputbox_list['template_type_id'] = "Service Implicit"
    DLT_templateID_dropdown_inputbox_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateID_dropdown_inputbox_list['template_sender_id'] = "123456"
    # DLT_templateID_dropdown_inputbox_list['template_message_id'] = "Normal"

    ################ Masking Check in user 11 #####################


class DLT_templateID_dropdown_masking:
    DLT_templateID_dropdown_masking_inputbox_list = {}
    DLT_templateID_dropdown_masking_inputbox_list['template_type_id'] = "Service Implicit"
    DLT_templateID_dropdown_masking_inputbox_list['template_entity_id'] = "OneTech(12**56)"


# ***********************Multiple tenant create********************************8
class DLT_templateIDEshort:
    DLT_templateIDEshort_inputbox_list = {}
    DLT_templateIDEshort_inputbox_list['template_name'] = "English Short"
    DLT_templateIDEshort_inputbox_list['template_id'] = "123456"
    DLT_templateIDEshort_inputbox_list['template_description'] = "It is a template for E short"
    DLT_templateIDEshort_inputbox_list['template_content'] = "select from dropdown English short"


class DLT_templateIDEshort_dropdown:
    DLT_templateIDEshort_dropdown_list = {}
    DLT_templateIDEshort_dropdown_list['template_type_id'] = "Service Implicit"
    DLT_templateIDEshort_dropdown_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateIDEshort_Promo_dropdown_list['template_sender_id'] = "123456"
    # DLT_templateIDEshort_Promo_dropdown_list['template_message_id'] = "Normal"


# ------------------------>>>  english short promo << ------------------------------


class DLT_templateIDEshort_Promo:
    DLT_templateIDEshort_Promo_inputbox_list = {}
    DLT_templateIDEshort_Promo_inputbox_list['template_name'] = "English Promo"
    DLT_templateIDEshort_Promo_inputbox_list['template_id'] = "9988776"
    DLT_templateIDEshort_Promo_inputbox_list['template_description'] = "It is a template for Promo short"
    DLT_templateIDEshort_Promo_inputbox_list['template_content'] = "Hello {#var#}, Welcome."


class DLT_templateIDEshort_Promo_dropdown:
    DLT_templateIDEshort_Promo_dropdown_list = {}
    DLT_templateIDEshort_Promo_dropdown_list['template_type_id'] = "Promo"
    DLT_templateIDEshort_Promo_dropdown_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateIDEshort_Promo_dropdown_list['template_sender_id'] = "123456"
    # DLT_templateIDEshort_Promo_dropdown_list['template_message_id'] = "Normal"


# ------------------->>>>     <<<<----------------------------------------

class DLT_templateID1:
    DLT_templateID1_inputbox_list = {}
    DLT_templateID1_inputbox_list['template_name'] = "Hindi Short"
    DLT_templateID1_inputbox_list['template_id'] = "12345678"
    DLT_templateID1_inputbox_list['template_description'] = "It is a template for h short"
    DLT_templateID1_inputbox_list[
        'template_content'] = "इस लेख में हम आपको 9वीं कक्षा के लेखन कौशल के विषय ‘सन्देश लेखन’ के बारे में बता रहे हैं।"


class DLT_templateID_dropdown11:
    DLT_templateID_dropdown11_inputbox_list = {}
    DLT_templateID_dropdown11_inputbox_list['template_type_id'] = "Service Implicit"
    DLT_templateID_dropdown11_inputbox_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateID_dropdown11_inputbox_list['template_sender_id'] = "123456"
    # DLT_templateID_dropdown11_inputbox_list['template_message_id'] = "Unicode"


class DLT_templateID2:
    DLT_templateID2_inputbox_list = {}
    DLT_templateID2_inputbox_list['template_name'] = "Hindi Long"
    DLT_templateID2_inputbox_list['template_id'] = "123456789"
    DLT_templateID2_inputbox_list['template_description'] = "It is a template for h long"
    DLT_templateID2_inputbox_list[
        'template_content'] = "{#var#} इस लेख में हम आपको 9वीं कक्षा के लेखन कौशल के विषय ‘सन्देश लेखन’ के बारे में बता रहे हैं। इस लेख में हम आपको, संदेश लेखन क्या होते हैं, संदेश लिखने के कौन से कारण होते हैं, संदेश लेखन के प्रकार कौन-कौन से हैं, संदेश लेखन के वक्त किन बातों का ध्यान रखना चाहिए और संदेश लेखन का प्रारूप व कुछ उदाहरण बताएँगे। आशा करते हैं कि हमारा यह लेख आपकी ‘सन्देश लेखन’ सम्बंधित सभी कठिनाइयों को दूर करने में सहायक सिद्ध होगा।"


class DLT_templateID_dropdown22:
    DLT_templateID_dropdown22_inputbox_list = {}
    DLT_templateID_dropdown22_inputbox_list['template_type_id'] = "Service Implicit"
    DLT_templateID_dropdown22_inputbox_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateID_dropdown22_inputbox_list['template_sender_id'] = "123456"
    # DLT_templateID_dropdown22_inputbox_list['template_message_id'] = "Unicode"


class DLT_templateID3:
    DLT_templateID3_inputbox_list = {}
    DLT_templateID3_inputbox_list['template_name'] = "One Variable"
    DLT_templateID3_inputbox_list['template_id'] = "1234567890"
    DLT_templateID3_inputbox_list['template_description'] = "It is a template for One Variable"
    DLT_templateID3_inputbox_list['template_content'] = "Hello {#var#}, Welcome."


class DLT_templateID_dropdown33:
    DLT_templateID_dropdown33_inputbox_list = {}
    DLT_templateID_dropdown33_inputbox_list['template_type_id'] = "Service Implicit"
    DLT_templateID_dropdown33_inputbox_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateID_dropdown33_inputbox_list['template_sender_id'] = "123456"
    # DLT_templateID_dropdown33_inputbox_list['template_message_id'] = "Normal"


class DLT_templateID4:
    DLT_templateID4_inputbox_list = {}
    DLT_templateID4_inputbox_list['template_name'] = "Three Variable"
    DLT_templateID4_inputbox_list['template_id'] = "12345678901"
    DLT_templateID4_inputbox_list['template_description'] = "It is a template for Three Variable"
    DLT_templateID4_inputbox_list[
        'template_content'] = "Hello {#var#}, Welcome To {#var#} and Ready For The Trip To {#var#}. {#var#} {#var#} {#var#}"


class DLT_templateID_dropdown44:
    DLT_templateID_dropdown44_inputbox_list = {}
    DLT_templateID_dropdown44_inputbox_list['template_type_id'] = "Service Implicit"
    DLT_templateID_dropdown44_inputbox_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateID_dropdown44_inputbox_list['template_sender_id'] = "123456"
    # DLT_templateID_dropdown44_inputbox_list['template_message_id'] = "Normal"


class DLT_templateID5:
    DLT_templateID5_inputbox_list = {}
    DLT_templateID5_inputbox_list['template_name'] = "Hindi One Variable"
    DLT_templateID5_inputbox_list['template_id'] = "123456789012"
    DLT_templateID5_inputbox_list['template_description'] = "It is a template for Hindi One Variable"
    DLT_templateID5_inputbox_list['template_content'] = "{#var#} कौशल"


class DLT_templateID_dropdown55:
    DLT_templateID_dropdown55_inputbox_list = {}
    DLT_templateID_dropdown55_inputbox_list['template_type_id'] = "Service Implicit"
    DLT_templateID_dropdown55_inputbox_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateID_dropdown55_inputbox_list['template_sender_id'] = "123456"
    # DLT_templateID_dropdown55_inputbox_list['template_message_id'] = "Normal"


######################  Promo hindi 1 var ############################

class DLT_templateIDPromo:
    DLT_templateIDPromo_inputbox_list = {}
    DLT_templateIDPromo_inputbox_list['template_name'] = "Promo Hindi"
    DLT_templateIDPromo_inputbox_list['template_id'] = "7766554"
    DLT_templateIDPromo_inputbox_list['template_description'] = "It is a template for Hindi One Variable"
    DLT_templateIDPromo_inputbox_list['template_content'] = "{#var#} कौशल"


class DLT_templateID_Promo_dropdown:
    DLT_templateID_Promo_dropdown_inputbox_list = {}
    DLT_templateID_Promo_dropdown_inputbox_list['template_type_id'] = "Promo"
    DLT_templateID_Promo_dropdown_inputbox_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateID_dropdown55_inputbox_list['template_sender_id'] = "123456"
    # DLT_templateID_dropdown55_inputbox_list['template_message_id'] = "Normal"


#####################################################################

class DLT_templateID6:
    DLT_templateID6_inputbox_list = {}
    DLT_templateID6_inputbox_list['template_name'] = "Long Three Var"
    DLT_templateID6_inputbox_list['template_id'] = "1234567890123"
    DLT_templateID6_inputbox_list['template_description'] = "It is a template for Three Variable"
    DLT_templateID6_inputbox_list[
        'template_content'] = "Message Writing is one of the common formal types of writing that we learn in our school curriculum {#var#} . {#var#} can be simply described as certain information we need to give to a person when we can't directly communicate or contact them. The format of a message mainly comprises elements like date, time, receiver's name, the message and then the sender's name. This blog brings you all the details about message writing format, practice questions and more!"


class DLT_templateID_dropdown66:
    DLT_templateID_dropdown66_inputbox_list = {}
    DLT_templateID_dropdown66_inputbox_list['template_type_id'] = "Service Implicit"
    DLT_templateID_dropdown66_inputbox_list['template_entity_id'] = "Onextel(123)"
    # DLT_templateID_dropdown55_inputbox_list['template_sender_id'] = "123456"
    # DLT_templateID_dropdown55_inputbox_list['template_message_id'] = "Normal"


class DLT_URL:
    DLT_URL_inputbox_list = {}
    DLT_URL_inputbox_list['url_name'] = "google.com"


# ****************************** No Record Found Check DLT Search **********************
class DLT_search:
    DLT_search_list = {}
    DLT_search_list["/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[1]"] = "English Long"

    # DLT_search_list["//*[@id='pills-campaign']/div[2]/div/span"] = "No Record Found"


# ***************************** All in one***********************************************************
class login:
    User_logins = {}
    User_logins['onexsa'] = "onexsa"


# ***************************** Context Based page load *********************************************
class page_load:
    User_logins = {}
    User_logins['onexsa'] = "onexsa"
    User_logins['Onexadmin'] = 'ali'
    User_logins["ICICIAdmin"] = "ali"

    list_onexsa = ["http://localhost:8000/dashboard", "http://localhost:8000/users",
                   "http://localhost:8000/credit_allocation", "http://localhost:8000/master_balance",
                   "http://localhost:8000/master_license"]
    list_href_links = ["/dashboard", "/users", "/credit_allocation", "/master_balance",
                       "/master_license"]

    list_tenant = ["http://localhost:8000/dashboard", "http://localhost:8000/users",
                   "http://localhost:8000/credit_allocation", "http://localhost:8000/report",
                   "http://localhost:8000/hub", "http://localhost:8000/test_sms", "http://localhost:8000/monitor"]
    list_tenant_href_links = ["/dashboard", "/users", "/credit_allocation", "/report", "/hub", "/test_sms", "/monitor"]

    list_tuc = ["http://localhost:8000/dashboard", "http://localhost:8000/campaign", "http://localhost:8000/users",
                "http://localhost:8000/credit_allocation", "http://localhost:8000/report",
                "http://localhost:8000/manage", "http://localhost:8000/smpps_view", "http://localhost:8000/api",
                "http://localhost:8000/phonebook",
                "http://localhost:8000/test_sms"]
    list_tuc_href_links = ["/dashboard", "/campaign", "/users", "/credit_allocation", "/report", "/manage",
                           "/smpps_view", "/api", "/phonebook", "/test_sms"]


class page_id:
    page_id_onexsa_list = {}
    page_id_onexsa_list['menu_dashboard'] = "/dashboard"
    page_id_onexsa_list['menu_users'] = "/users"
    page_id_onexsa_list['menu_credit_allocation'] = "/credit_allocation"
    page_id_onexsa_list['menu_master_balance'] = "/master_balance"
    page_id_onexsa_list['menu_master_license'] = "/master_license"


class page_tenant_id:
    page_id_tenant_list = {}
    page_id_tenant_list['menu_dashboard'] = "/dashboard"
    page_id_tenant_list['menu_users'] = "/users"
    page_id_tenant_list['menu_credit_allocation'] = "/credit_allocation"
    page_id_tenant_list['menu_report'] = "/report"
    page_id_tenant_list['menu_hub'] = "/hub"
    page_id_tenant_list['menu_test_sms'] = "/test_sms"
    page_id_tenant_list['menu_monitor'] = "/monitor"


class page_tuc_id:
    page_id_tuc_list = {}
    page_id_tuc_list['menu_dashboard'] = "/dashboard"
    page_id_tuc_list['menu_users'] = "/users"
    page_id_tuc_list['menu_credit_allocation'] = "/credit_allocation"
    page_id_tuc_list['menu_report'] = "/report"
    page_id_tuc_list['menu_manage'] = "/manage"
    page_id_tuc_list['menu_smpps_view'] = "/smpps_view"
    page_id_tuc_list['menu_api'] = "/api"
    page_id_tuc_list['menu_phonebook'] = "/phonebook"
    page_id_tuc_list['menu_test_sms'] = "/test_sms"


# ****************** Log Out ******************
class Login_Logout:
    User_logins = {}
    User_logins['onexsa'] = "onexsa"
    User_logins['Onexadmin'] = 'ali'
    User_logins["ICICIAdmin"] = "ali"

    list_onexsa = []
    list_onexsa.append("")
    list_onexsa.append("")


# **************************** Phonebook *******************************************

class phonebook:
    phonebook_inputbox_list = {}
    phonebook_inputbox_list['available_credits'] = "0"
    phonebook_inputbox_list['current_date'] = current_Day_Date
    phonebook_inputbox_list['senderid_tab'] = "Sender IDs"
    phonebook_inputbox_list['template_tab'] = "Template"
    phonebook_inputbox_list['url_tab'] = "URL"
    phonebook_inputbox_list['domain_tab'] = "Domain"


# def FindAllId(context):
#     ids = context.driver.find_elements_by_xpath('//*[@id]')
#     for ii in ids:
#         # print ii.tag_name
#         print(ii.get_attribute('id'))


# ******************************** All Alocation *********************************

class all_allocation:
    all_allocation_inputbox_list = {}
    all_allocation_inputbox_list['available_credits'] = "0"
    all_allocation_inputbox_list['current_date'] = current_Day_Date
    all_allocation_inputbox_list['date1'] = "From"
    all_allocation_inputbox_list['date2'] = "To"

    all_allocation_inputbox_list['search_alloc'] = "button"
    all_allocation_inputbox_list['available_credits'] = "0"


class master_bal_error_label:
    master_bal_error_label_list = {}
    # master_bal_error_label_list["//*[@id='myModal']/div/div/div[2]/div/label/span"] = "Amount must not be Empty !"
    master_bal_error_label_list["//*[@id='myModal']/div/div/div[2]/div/label/span"] = "Credits* must not be Empty !"
    master_bal_error_label_list["//*[@id='cancel']"] = " Cancel"


class practise1:
    practise1_label_error_list = {}
    practise1_label_error_list["//*[@id='myModal']/div/div/div[2]/div[2]/span/span"] = "Amount is incorrect"
    practise1_label_error_list["//*[@id='cancel']"] = " Cancel"

    amount_list = [" ", "0", "-1", "19999999990", "444.3", "alpha 786"]
    error_list = []


class label_chekc:
    error_label_chekc = {}
    error_label_chekc['onexsa'] = "onexsa"
    amount_list = [" ", "0", "-1", "1000000000", "10000000000", "44.44", "-1"]


class label_xpath:
    label_xpath_master_list = {}
    label_xpath_master_list['menu_dashboard'] = "/dashboard"
    label_xpath_master_list['menu_users'] = "/users"
    label_xpath_master_list['menu_credit_allocation'] = "/credit_allocation"
    label_xpath_master_list['menu_master_balance'] = "/master_balance"
    label_xpath_master_list['menu_master_license'] = "/master_license"


# ++++++++++++++++++++++++Check Cancel Button is working in all pages+++++++++++++++++++++++++++

class cancel_buuton:
    User_logins = {}
    User_logins['onexsa'] = "onexsa"
    User_logins['Onexadmin'] = 'ali'
    User_logins["ICICIAdmin"] = "ali"

    list_cancel_buuton = ["http://localhost:8000/dashboard", "http://localhost:8000/users",
                          "http://localhost:8000/credit_allocation", "http://localhost:8000/master_balance",
                          "http://localhost:8000/master_license", "http://localhost:8000/test_sms"]
    list_href_links = ["/dashboard", "/users", "/credit_allocation", "/master_balance",
                       "/master_license", "/test_sms"]


# *****************************Approvals**************************************
class Approvals:
    Approvals_label_list = {}
    Approvals_label_list['pills-pending-tab'] = "Pending"
    Approvals_label_list['pills-approved-tab'] = "Approved"
    Approvals_label_list['pills-not-approved-tab'] = "Rejected"


# ****************************New SMS*************************************************
class new_sms:
    new_sms_label_list = {}
    new_sms_label_list['quick_sms_page_link'] = "tab"
    new_sms_label_list['unicode_sms_page_link'] = "tab"
    new_sms_label_list['dynamic_sms_page_link'] = "tab"
    new_sms_label_list['campaign_sms_page_link'] = "tab"
    new_sms_label_list['current_date'] = "date"


class new_quick_sms:
    new_quick_sms_list = {}
    new_quick_sms_list['campaign_name'] = "RCF"
    new_quick_sms_list['sender_id'] = "123456"
    new_quick_sms_list['recipient_numbers'] = "9234567890"
    new_quick_sms_list['msgText'] = "tab"
    new_quick_sms_list['Clear'] = "tab"
    new_quick_sms_list['Clear'] = "tab"
    new_quick_sms_list['insert_template'] = "Insert Template"
    new_quick_sms_list['cancel'] = "tab"
    new_quick_sms_list['send'] = "tab"
    new_quick_sms_list['available_credits'] = "0"


class new_quick_sms_input:
    new_quick_sms_input_list = {}
    new_quick_sms_input_list['campaign_name'] = "RCF"
    new_quick_sms_input_list['sender_id'] = "123456"
    new_quick_sms_input_list['recipient_numbers'] = "9234567890"

    #################  unicode long without recipients data ###############


class new_quick_sms_input_no_recipients:
    new_quick_sms_input_no_recipients_list = {}
    new_quick_sms_input_no_recipients_list['campaign_name'] = "RCF"
    new_quick_sms_input_no_recipients_list['sender_id'] = "123456"

    ##########################################################################


class new_quick_sms_input1:
    new_quick_sms_input1_list = {}
    new_quick_sms_input1_list['campaign_name'] = "RCF"
    new_quick_sms_input1_list['sender_id'] = "123456"
    new_quick_sms_input1_list['recipient_numbers'] = "9123456789 \n 8527406188 \n 8292037493 \n 8209726233"


# -------------------->> Promo sms input << -------------------------

class new_quick_sms_Promo_input:
    new_quick_sms_Promo_input1_list = {}
    new_quick_sms_Promo_input1_list['campaign_name'] = "RCF"
    new_quick_sms_Promo_input1_list['sender_id'] = "123456"
    new_quick_sms_Promo_input1_list['recipient_numbers'] = "9123456789 \n 8527406188 \n 8292037493 \n 8209726233"


######################################################################

class new_quick_sms_input2:
    new_quick_sms_input2_list = {}
    new_quick_sms_input2_list['campaign_name'] = "default(2200)"
    new_quick_sms_input2_list['sender_id'] = "123456"


class new_quick_sms_input3:
    new_quick_sms_input3_list = {}
    new_quick_sms_input3_list['campaign_name'] = "default(2200)"
    new_quick_sms_input3_list['sender_id'] = "123456"
    new_quick_sms_input3_list['recipient_numbers'] = "9123456789 \n 8527406188 \n 8292037493 \n 8209726233"


class new_quick_sms_group:
    new_quick_sms_group_list = {}
    new_quick_sms_group_list['campaign_name'] = "RCF"
    new_quick_sms_group_list['sender_id'] = "123456"


class new_quick_sms_input3:
    new_quick_sms_input3_list = {}
    new_quick_sms_input3_list['campaign_name'] = "default(2200)"
    new_quick_sms_input3_list['sender_id'] = "123456"
    new_quick_sms_input3_list['recipient_numbers'] = "9123456789 \n 8527406188 \n 8292037493 \n 8209726233"


class new_quick_sms_input33:
    new_quick_sms_input33_list = {}
    new_quick_sms_input33_list['campaign_name'] = "RCF"
    new_quick_sms_input33_list['sender_id'] = "123456"


###############  Executed file 1 #######################

class executed_campaign_input:
    executed_campaign_input_list = {}
    executed_campaign_input_list['campaign_name'] = "RCF"
    executed_campaign_input_list['sender_id'] = "098765"
    executed_campaign_input_list['recipient_numbers'] = "8527406188"

    ###################################################


class new_quick_sms_insert_template:
    new_quick_sms_insert_template_label_list = {}
    new_quick_sms_insert_template_label_list['template_name'] = "RCF"
    new_quick_sms_insert_template_label_list['template_id'] = "123456"
    new_quick_sms_insert_template_label_list['parameter'] = "9234567890"
    # new_quick_sms_insert_template_label_list['message-text'] = "tab"
    new_quick_sms_insert_template_label_list['cancel_modal'] = "qweerr"
    new_quick_sms_insert_template_label_list['insert_template'] = "1234567890"
    new_quick_sms_insert_template_label_list['close_modal'] = "tab"


# *************************Multiple Quick SMS*************************************
class new_multiple_quick_sms_input:
    new_multiple_quick_sms_input = {}
    new_multiple_quick_sms_input['campaign_name'] = "RCF"
    new_multiple_quick_sms_input['sender_id'] = "123456"
    new_multiple_quick_sms_input['recipient_numbers'] = "8605493727"


# *********************** Dynamic SMS ****************************************
class new_dynamic_sms:
    new_dynamic_sms_input = {}
    new_dynamic_sms_input['campaign_name'] = "RCF"
    new_dynamic_sms_input['sender_id'] = "123456"


# *****************************NEW Campaign SMS ***************************************
class new_campaign_sms:
    new_campaign_sms_list = {}
    new_campaign_sms_list['campaign_name'] = "RCF"
    new_campaign_sms_list['sender_id'] = "123456"
    new_campaign_sms_list['msgText'] = "tab"
    new_campaign_sms_list['Clear'] = "tab"
    new_campaign_sms_list['Clear'] = "tab"
    # new_quick_sms_list['insert_url'] = "Insert URL"
    new_campaign_sms_list['insert_template'] = "Insert Template"
    new_campaign_sms_list['cancel'] = "tab"
    new_campaign_sms_list['save_as_draft'] = "tab"
    new_campaign_sms_list['send'] = "tab"
    new_campaign_sms_list['available_credits'] = "0"


class new_campaign_sms_checkbox:
    new_campaign_sms_checkbox_list = {}
    new_campaign_sms_checkbox_list['duplicate_check'] = "RCF"
    new_campaign_sms_checkbox_list['invalid_check'] = "123456"
    new_campaign_sms_checkbox_list['multipart_check'] = "1234567890"
    new_campaign_sms_checkbox_list['unicode_check'] = "tab"
    new_campaign_sms_checkbox_list['flash_check'] = "tab"
    new_campaign_sms_checkbox_list['schedule_check'] = "tab"


class new_campaign_sms_input:
    new_campaign_sms_input_list = {}
    new_campaign_sms_input_list['campaign_name'] = "RCF"
    new_campaign_sms_input_list['sender_id'] = "123456"


# ************************Unicode SMS******************************************
class new_unicode_sms:
    new_unicode_sms_list = {}
    new_unicode_sms_list['campaign_name'] = "RCF"
    new_unicode_sms_list['sender_id'] = "123456"
    new_unicode_sms_list['recipient_numbers'] = "1234567890"
    new_unicode_sms_list['msgText'] = "tab"
    new_unicode_sms_list['Clear'] = "tab"
    new_unicode_sms_list['Clear'] = "tab"
    new_unicode_sms_list['insert_template'] = "Insert Template"
    new_unicode_sms_list['cancel'] = "tab"
    new_unicode_sms_list['send'] = "tab"
    new_unicode_sms_list['available_credits'] = "0"


class new_unicode_sms_checkbox:
    new_unicode_sms_checkbox_list = {}
    new_unicode_sms_checkbox_list['duplicate_check'] = "RCF"
    new_unicode_sms_checkbox_list['invalid_check'] = "123456"
    new_unicode_sms_checkbox_list['multipart_check'] = "1234567890"
    new_unicode_sms_checkbox_list['unicode_check'] = "tab"
    new_unicode_sms_checkbox_list['flash_check'] = "tab"
    new_unicode_sms_checkbox_list['flash_check'] = "tab"


class new_unicode_sms_input:
    new_unicode_sms_input_list = {}
    new_unicode_sms_input_list['campaign_name'] = "RCF"
    new_unicode_sms_input_list['sender_id'] = "123456"
    new_unicode_sms_input_list['recipient_numbers'] = "8292037493"


# *******************************Dynamic SMS*******************************************
class new_dynamic_sms:
    new_dynamic_sms_list = {}
    new_dynamic_sms_list['campaign_name'] = "RCF"
    new_dynamic_sms_list['sender_id'] = "123456"
    # new_dynamic_sms_list['recipient_numbers'] = "1234567890"
    new_dynamic_sms_list['msgText'] = "tab"
    new_dynamic_sms_list['Clear'] = "tab"
    # new_dynamic_sms_list['clear'] = "tab"
    new_dynamic_sms_list['insert_template'] = "Insert Template"
    new_dynamic_sms_list['cancel'] = "tab"
    new_dynamic_sms_list['send'] = "tab"
    new_dynamic_sms_list['available_credits'] = "0"


class new_dynamic_sms_checkbox:
    new_dynamic_sms_checkbox_list = {}
    # new_dynamic_sms_checkbox_list['duplicate_check'] = "RCF"
    new_dynamic_sms_checkbox_list['invalid_check'] = "123456"
    new_dynamic_sms_checkbox_list['multipart_check'] = "1234567890"
    new_dynamic_sms_checkbox_list['unicode_check'] = "tab"
    new_dynamic_sms_checkbox_list['flash_check'] = "tab"
    new_dynamic_sms_checkbox_list['flash_check'] = "tab"


class new_dynamic_sms_input:
    new_unicode_sms_input_list = {}
    new_unicode_sms_input_list['campaign_name'] = "RCF"
    new_unicode_sms_input_list['sender_id'] = "123456"
    # new_unicode_sms_input_list['recipient_numbers'] = "1234567890"


# *********************************** SMPP *****************************************
class SMPP:
    smpp_label_list = {}
    smpp_label_list['smpps_view'] = "SMPPS"
    smpp_label_list['bind_history'] = "Bind History"
    smpp_label_list['create_smpps'] = "+Add SMPPS"
    smpp_label_list['current_date'] = current_Day_Date


class SMPP_SMPPS:
    SMPP_SMPPS_inputbox_list = {}
    SMPP_SMPPS_inputbox_list['systemid'] = "2"
    SMPP_SMPPS_inputbox_list['password'] = "ali"
    SMPP_SMPPS_inputbox_list['systemtype'] = "loan"
    SMPP_SMPPS_inputbox_list['accounttype'] = "TRANSPROMO"
    SMPP_SMPPS_inputbox_list['limitday'] = "1"
    SMPP_SMPPS_inputbox_list['limithour'] = "1"
    SMPP_SMPPS_inputbox_list['validity'] = "1"
    SMPP_SMPPS_inputbox_list['templateId'] = "1"
    SMPP_SMPPS_inputbox_list['entityId'] = "1"
    SMPP_SMPPS_inputbox_list['total_tps'] = "1"
    SMPP_SMPPS_inputbox_list['keep_alive'] = "1"
    SMPP_SMPPS_inputbox_list['max_binds'] = "1"
    # SMPP_SMPPS_Edit_inputbox_list['save_smpps'] = "Button"
    # SMPP_SMPPS_Edit_inputbox_list['cancel'] = "Button"
    # SMPP_SMPPS_Edit_inputbox_list['otherpanel1'] = "Label"

    ################### for promo ######################


class SMPP_SMPPS_Promo:
    SMPP_SMPPS_Promo_inputbox_list = {}
    SMPP_SMPPS_Promo_inputbox_list['systemid'] = "promo"
    SMPP_SMPPS_Promo_inputbox_list['password'] = "ali"
    SMPP_SMPPS_Promo_inputbox_list['systemtype'] = "loan"
    SMPP_SMPPS_Promo_inputbox_list['accounttype'] = "Promotional"
    SMPP_SMPPS_Promo_inputbox_list['limitday'] = "1"
    SMPP_SMPPS_Promo_inputbox_list['limithour'] = "1"
    SMPP_SMPPS_Promo_inputbox_list['validity'] = "1"
    SMPP_SMPPS_Promo_inputbox_list['templateId'] = "1"
    SMPP_SMPPS_Promo_inputbox_list['entityId'] = "1"
    SMPP_SMPPS_Promo_inputbox_list['total_tps'] = "1"
    SMPP_SMPPS_Promo_inputbox_list['keep_alive'] = "1"
    SMPP_SMPPS_Promo_inputbox_list['max_binds'] = "1"
    # SMPP_SMPPS_Edit_inputbox_list['save_smpps'] = "Button"
    # SMPP_SMPPS_Edit_inputbox_list['cancel'] = "Button"
    # SMPP_SMPPS_Edit_inputbox_list['otherpanel1'] = "Label"


################### SMPP Edit ######################

class SMPP_SMPPS_Edit:
    SMPP_SMPPS_Edit_inputbox_list = {}
    SMPP_SMPPS_Edit_inputbox_list['systemid'] = "Edited"
    SMPP_SMPPS_Edit_inputbox_list['password'] = "ali"
    SMPP_SMPPS_Edit_inputbox_list['systemtype'] = "OTP"
    # SMPP_SMPPS_Edit_inputbox_list['accounttype'] = "OTPOTP"

    # SMPP_SMPPS_Edit_inputbox_list['save_smpps'] = "Button"
    # SMPP_SMPPS_Edit_inputbox_list['cancel'] = "Button"
    # SMPP_SMPPS_Edit_inputbox_list['otherpanel1'] = "Label"


# ***********************************PhoneBook***********************************

class phonebook:
    phonebook_label_list = {}
    # phonebook_label_list['phonebook_group'] = "Group"
    phonebook_label_list['groups'] = "Group"
    # phonebook_label_list['phonebook_contact'] = "Contacts"
    phonebook_label_list['contacts'] = "Contacts"
    # phonebook_label_list['phonebook_blacklist'] = "Blacklisted"
    # phonebook_label_list['blacklisted'] = "Blacklisted"  #**Now Removed***
    # phonebook_label_list['create_group'] = "+ Add Group"
    phonebook_label_list['add-group'] = "+ Add Group"
    phonebook_label_list['current_date'] = current_Day_Date


class phonebook_group:
    phonebook_group_inputbox_list = {}
    phonebook_group_inputbox_list['group-name'] = "abc"
    phonebook_group_inputbox_list['group-desc'] = "xyz"
    # phonebook_group_inputbox_list['add'] = "Blacklisted"
    # phonebook_group_inputbox_list['cancel'] = "+ Add Group"


class phonebook_contact:
    phonebook_contact_label_list = {}
    # phonebook_contact_label_list['select_group'] = "dropdown"
    phonebook_contact_label_list['group-select'] = "dropdown"
    # phonebook_contact_label_list['create_contact'] = "+ Add Contact"
    phonebook_contact_label_list['add-contacts'] = "+ Add Contact"
    phonebook_contact_label_list['current_date'] = current_Day_Date


class phonebook_add_single_contact:
    phonebook_add_single_contact_list = {}
    phonebook_add_single_contact_list['name'] = "Jay"
    phonebook_add_single_contact_list['number'] = "1234567890"
    phonebook_add_single_contact_list['select-group-single'] = "abc(500)"
    phonebook_add_single_contact_list['add'] = "+ Add Contact"
    phonebook_add_single_contact_list['cancel'] = "cancel button"
    phonebook_add_single_contact_list['addcontact'] = "label"


class phonebook_add_single_contact_inout:
    phonebook_add_single_contact_inout_list = {}
    phonebook_add_single_contact_inout_list['name'] = "Jay"
    phonebook_add_single_contact_inout_list['number'] = "1234567890"
    phonebook_add_single_contact_inout_list['select-group-single'] = "abc(500)"


class select_group:
    select_group_list = {}
    # select_group_list["//*[@id='contact-table']/tbody/tr[2]/td[3]"] = "1234567890"
    select_group_list["//*[@id='contacts-table']/tbody/tr[2]/td[3]"] = "6262923192"
    select_group_list["//*[@id='current_date']"] = current_Day_Date


#################################Profile Account/Setting#############################################
class profile_my_account:
    profile_my_account_list = {}
    profile_my_account_list["profile-fname"] = "Onexsa"
    profile_my_account_list["profile-lname"] = "Admin"
    profile_my_account_list["profile-company"] = "OneXTel Pvt"
    profile_my_account_list["profile-email"] = "sa@onextel.tech"
    profile_my_account_list["profile-phone"] = "1234567"
    profile_my_account_list["profile-email"] = "sa@onextel.tech"
    profile_my_account_list["save-changes"] = "save-btn"
    profile_my_account_list["available_credits"] = "1,00,000"


class profile_alert:
    profile_alert_list = {}
    # profile_alert_list["du"] = "Daily Usage"
    # profile_alert_list["wu"] = "Weekly Usage"
    # profile_alert_list["mdwu"] = "Monthly Day-wise Usage"
    # profile_alert_list["mtu"] = "Monthly Day-wise Usage"
    # profile_alert_list["lbabs"] = "Low Balance alert by SMS"
    # profile_alert_list["lbabe"] = "Low Balance alert by Email"
    profile_alert_list["//*[@id='pills-alerts']/div/div/div/div/p[1]"] = "Low Credit alert by Email"
    # profile_alert_list["wtr"] = "Weekly Transaction Report"
    # profile_alert_list["mtr"] = "Monthly Transaction Report"

    list_edit = ["du", "wu", "mdwu", "mtu", "lbabs", "lbabe", "wtr", "mtr"]


class profile_change_password:
    profile_change_password_list = {}
    profile_change_password_list["current-pwd"] = "onextel"
    profile_change_password_list["currentPassword"] = "curr pass eye button"
    profile_change_password_list["new-pwd"] = "onexsa"
    profile_change_password_list["newPassword"] = "new pass eye button "
    profile_change_password_list["renter-pwd"] = "onexsa"
    profile_change_password_list["reEnteredPassword"] = "re enter pass eye button"
    profile_change_password_list["change-num-email"] = "submit request"
    profile_change_password_list["available_credits"] = "1,00,000"


class profile_change_password_edit:
    profile_change_password_edit_list = {}
    profile_change_password_edit_list["current-pwd"] = "onextel"
    profile_change_password_edit_list["new-pwd"] = "onexsa"
    profile_change_password_edit_list["renter-pwd"] = "onexsa"


# *********************** Report ****************************************

class Report:
    Report_list = {}
    Report_list['pills-mis-data-tab'] = "MIS"
    Report_list['pills-summary-tab'] = "Summary"
    Report_list['pills-campaign-summary-tab'] = "Campaign Summary"
    Report_list['pills-search-tab'] = "Search"
    Report_list['pills-daily-summary-tab'] = "Sender ID Summary"
    Report_list['pills-latency-report-tab'] = "Latency Report"
    Report_list['pills-clicker-data-tab'] = "Clicker Data"
    Report_list['pills-campaign-tab'] = "Scheduled Campaigns"
    Report_list['pills-download-data-tab'] = "Download Data"
    # Report_list['create_entityid'] = current_Day_Datek


class Report_quick_search:
    Report_quick_search_list = {}
    Report_quick_search_list["//*[@id='search_label']"] = "Not able to get Data"
    # Report_quick_search_list["//*[@id='campaign-summary-table']/tbody/tr[2]/td[1]"] = "No report data avaialable"
    # Report_quick_search_list['/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/div[3]/input'] = "Enter uuid"


class Report_MIS_quick_search:
    Report_mis_quick_search_list = {}
    Report_mis_quick_search_list["//*[@id='pills-daily-summary']/div[3]"] = "No report data avaialable"
    # Report_quick_search_list['/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/div[3]/input'] = "Enter uuid"


# **************** TUC SMS Balance Deduction ************************************
class TUC_SMS_Balance_Deduction:
    TUC_SMS_Balance_Deduction_list = {}
    TUC_SMS_Balance_Deduction_list['available_credits'] = "953"
    TUC_SMS_Balance_Deduction_list['current_date'] = current_Day_Date


# ************ API ************************
class API_dropdown1:
    API_dropdown1_inputbox_list = {}
    # API_dropdown1_inputbox_list['//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "PROMO"
    API_dropdown1_inputbox_list['//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "Promotional"


class API_dropdown2:
    API_dropdown2_inputbox_list = {}
    # API_dropdown2_inputbox_list['//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "GOV"
    API_dropdown2_inputbox_list['//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "Government"


class API_dropdown3:
    API_dropdown3_inputbox_list = {}
    # API_dropdown3_inputbox_list['//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "TRANS"
    API_dropdown3_inputbox_list[
        '//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "Transactional"


class API_dropdown4:
    API_dropdown4_inputbox_list = {}
    API_dropdown4_inputbox_list[
        # '//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "SERVICE_IMPLICIT"
        '//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "Service Implicit"


class API_dropdown5:
    API_dropdown5_inputbox_list = {}
    API_dropdown5_inputbox_list[
        # '//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "SERVICE_EXPLICIT"
        '//*[@id="pills-campaign"]/div[1]/div[2]/div/div/div/div[2]/div/select'] = "Service Explicit"


# *************** OPTION TYPE **************
class Type1:
    Type1_inputbox_list = {}
    Type1_inputbox_list['type_atom'] = "otp"
    Type1_inputbox_list['type_name'] = "OTP"
    Type1_inputbox_list['type_desc'] = "qwerty"


class Type2:
    Type2_inputbox_list = {}
    Type2_inputbox_list['type_atom'] = "promo"
    Type2_inputbox_list['type_name'] = "PROMO"
    Type2_inputbox_list['type_desc'] = "qwerty"


class Type3:
    Type3_inputbox_list = {}
    Type3_inputbox_list['type_atom'] = "trans"
    Type3_inputbox_list['type_name'] = "TRANS"
    Type3_inputbox_list['type_desc'] = "qwerty"


class Type4:
    Type4_inputbox_list = {}
    Type4_inputbox_list['type_atom'] = "gov"
    Type4_inputbox_list['type_name'] = "GOV"
    Type4_inputbox_list['type_desc'] = "qwerty"


class Type5:
    Type5_inputbox_list = {}
    Type5_inputbox_list['type_atom'] = "serv_imp"
    Type5_inputbox_list['type_name'] = "SERVICE_IMPLICIT"
    Type5_inputbox_list['type_desc'] = "qwerty"


class Type6:
    Type6_inputbox_list = {}
    Type6_inputbox_list['type_atom'] = "serv_exp"
    Type6_inputbox_list['type_name'] = "SERVICE_EXPLICIT"
    Type6_inputbox_list['type_desc'] = "qwerty"


# **********TENANT OPTION*********************
class Option_Carrier_edit:
    Option_Carrier_edit_inputbox_list = {}
    Option_Carrier_edit_inputbox_list["carrier_name"] = "BSNL"
    Option_Carrier_edit_inputbox_list["carrier_desc"] = "This is BSNL company"


class Option_Circle_edit:
    Option_Circle_edit_inputbox_list = {}
    Option_Circle_edit_inputbox_list["circle_name"] = "BSNL"
    Option_Circle_edit_inputbox_list["circle_desc"] = "This is BSNL company"


class Option_Vendor_edit:
    Option_Vendor_edit_inputbox_list = {}
    Option_Vendor_edit_inputbox_list["vendor_name"] = "BSNL"
    Option_Vendor_edit_inputbox_list["vendor_telemar"] = "BSNL@telcom"
    Option_Vendor_edit_inputbox_list["vendor_desc"] = "This is BSNL company"


class Option_Type_edit:
    Option_Type_edit_inputbox_list = {}
    # Option_Type_edit_inputbox_list["type_atom"] = "Promo"
    # Option_Type_edit_inputbox_list["type_name"] = "PROMO"
    Option_Type_edit_inputbox_list["type_desc"] = "QWERTY"


############Vendor Special Char Add and Edit###########
class Option_Vendor_add:
    Option_Type_add_inputbox_list = {}
    Option_Type_add_inputbox_list["vendor_name"] = "Airtel"
    Option_Type_add_inputbox_list["vendor_telemar"] = "Airtel@telecom"
    Option_Type_add_inputbox_list["vendor_desc"] = "This is Airtel company"


class Option_Vendor_edit:
    Option_Vendor_edit_inputbox_list = {}
    Option_Vendor_edit_inputbox_list["vendor_name"] = "BSNL"
    Option_Vendor_edit_inputbox_list["vendor_telemar"] = "BSNL@telcom"
    Option_Vendor_edit_inputbox_list["vendor_desc"] = "This is BSNL company"


########### Notification #################
class Add_Notification:
    Add_Notification_inputbox_list = {}
    Add_Notification_inputbox_list["noitf_sub"] = "adding notification"
    Add_Notification_inputbox_list["noitf_text"] = "Notification from SA to ALL"
    Add_Notification_inputbox_list["enter_tuc"] = "2000"


class Edit_Notification:
    Edit_Notification_inputbox_list = {}
    Edit_Notification_inputbox_list["noitf_sub"] = "Edited notification"
    Edit_Notification_inputbox_list["noitf_text"] = "Edited notifcation from SA"


class Tuc_Add_Notification:
    Tuc_Add_Notification_inputbox_list = {}
    Tuc_Add_Notification_inputbox_list["noitf_sub"] = "adding notification"
    Tuc_Add_Notification_inputbox_list["noitf_text"] = "Notification from SA to ALL"
    Tuc_Add_Notification_inputbox_list["enter_tuc"] = "2002"


class Tuc_Edit_Notification:
    Tuc_Edit_Notification_inputbox_list = {}
    Tuc_Edit_Notification_inputbox_list["noitf_sub"] = "Edited notification"
    Tuc_Edit_Notification_inputbox_list["noitf_text"] = "Edited notifcation from Tuc"
