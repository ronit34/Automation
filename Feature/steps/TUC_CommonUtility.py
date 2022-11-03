from datetime import datetime
x = datetime.now()
current_Day_Date = (x.strftime("%A" " " "%d" " " "%B" " " "%Y"))

#******************************* ICICI Child Sales ***********************************
class ICICI_Child_sales:
    ICICI_Child_sales_list = {}
    ICICI_Child_sales_list['name'] = "SALES"
    # ICICI_Child_sales_list['cost_per_otp'] = "10"  ### Wallet Updated
    # ICICI_Child_sales_list['cost_per_tx'] = "60"
    # ICICI_Child_sales_list['cost_per_promo'] = "30"
    # ICICI_Child_sales_list['cost_per_simroute'] = "40"
    # ICICI_Child_sales_list['scrubbing_cost'] = "40"

    ICICI_Child_sales_list['otp_acc_type'] = "On Delivery"  #### Updated fields ######
    ICICI_Child_sales_list['trans_acc_type'] = "On Delivery"
    ICICI_Child_sales_list['promo_acc_type'] = "On Delivery"
    ICICI_Child_sales_list['gov_acc_type'] = "On Delivery"
    ICICI_Child_sales_list['sim_acc_type'] = "On Delivery"
    ICICI_Child_sales_list['default_acc_type'] = "On Delivery"

    ICICI_Child_sales_list['cost_unit'] = "paisa"
    # ICICI_Child_sales_list['accmgr'] = "sant"
    ICICI_Child_sales_list['billing_type'] = "POSTPAID"
    # ICICI_Child_sales_list['dlt_charges'] = "On Delivery"
    # ICICI_Child_sales_list['sms_charges'] = "On Delivery"
    ICICI_Child_sales_list['mask_phone'] = "Yes"
    ICICI_Child_sales_list['validity'] = "101"
    ICICI_Child_sales_list['childtuc'] = "10"
    ICICI_Child_sales_list['smpps'] = "10"
    ICICI_Child_sales_list['smsapi'] = "10"
    ICICI_Child_sales_list['cancel'] = " Cancel Button"
    ICICI_Child_sales_list['save_tuc'] = " Create Button"
    ICICI_Child_sales_list['save_tuc'] = " Create Button"

#******************************* ICICI Child Sales User ***********************************
class ICICI_Child_sales_user:
    ICICI_Child_sales_user_list = {}
    ICICI_Child_sales_user_list['username'] = "sales"
    ICICI_Child_sales_user_list['password'] = "sales"
    ICICI_Child_sales_user_list['fname'] = "sales"
    ICICI_Child_sales_user_list['lname'] = "department"
    ICICI_Child_sales_user_list['email'] = "xyz@gmail.com"
    ICICI_Child_sales_user_list['mob_no'] = "1234567890"
    ICICI_Child_sales_user_list['comp_name'] = "onextel"
    ICICI_Child_sales_user_list['web'] = "Onextel.tech"
    ICICI_Child_sales_user_list['other_mob_no'] = "1234567899"
    ICICI_Child_sales_user_list['role_type'] = "Tuc"
    ICICI_Child_sales_user_list['cancel'] = "Button"
    ICICI_Child_sales_user_list['tuc'] = "Button"
    ICICI_Child_sales_user_list['save_user'] = "Button"
    ICICI_Child_sales_user_list['save_user'] = "Button"

#******************************* ICICI Child----> Sales Child------>Loan Create ***********************************
class Sales_child_loan:
    Sales_child_loan_list = {}
    Sales_child_loan_list['name'] = "loan"
    # Sales_child_loan_list['cost_per_otp'] = "10"
    # Sales_child_loan_list['cost_per_tx'] = "60"
    # Sales_child_loan_list['cost_per_promo'] = "30"
    # Sales_child_loan_list['cost_per_simroute'] = "40"
    # Sales_child_loan_list['scrubbing_cost'] = "40"

    Sales_child_loan_list['otp_acc_type'] = "On Delivery"  #### Updated fields
    Sales_child_loan_list['trans_acc_type'] = "On Delivery"
    Sales_child_loan_list['promo_acc_type'] = "On Delivery"
    Sales_child_loan_list['gov_acc_type'] = "On Delivery"
    Sales_child_loan_list['sim_acc_type'] = "On Delivery"
    Sales_child_loan_list['default_acc_type'] = "On Delivery"

    Sales_child_loan_list['cost_unit'] = "paisa"
    # Sales_child_loan_list['accmgr'] = "sant"
    Sales_child_loan_list['billing_type'] = "POSTPAID"
    # Sales_child_loan_list['dlt_charges'] = "On Delivery"
    # Sales_child_loan_list['sms_charges'] = "On Delivery"
    Sales_child_loan_list['mask_phone'] = "Yes"
    Sales_child_loan_list['validity'] = "101"
    # Sales_child_loan_list['childtuc'] = "5"
    Sales_child_loan_list['childtuc'] = "0"
    Sales_child_loan_list['smpps'] = "5"
    Sales_child_loan_list['smsapi'] = "5"
    Sales_child_loan_list['cancel'] = " Cancel Button"
    Sales_child_loan_list['save_tuc'] = " Create Button"
    Sales_child_loan_list['save_tuc'] = " Create Button"

#******************************* ICICI Child----> Sales Child------>Loan User ***********************************
class Sales_child_loan_user:
    Sales_child_loan_user_list = {}
    Sales_child_loan_user_list['username'] = "loan"
    Sales_child_loan_user_list['password'] = "loan"
    Sales_child_loan_user_list['fname'] = "credit"
    Sales_child_loan_user_list['lname'] = "amt"
    Sales_child_loan_user_list['email'] = "xyz@gmail.com"
    Sales_child_loan_user_list['mob_no'] = "1234567890"
    Sales_child_loan_user_list['comp_name'] = "onextel"
    Sales_child_loan_user_list['web'] = "Onextel.tech"
    Sales_child_loan_user_list['other_mob_no'] = "1234567899"
    Sales_child_loan_user_list['role_type'] = "Tuc"
    Sales_child_loan_user_list['cancel'] = "Button"
    Sales_child_loan_user_list['tuc'] = "Button"
    Sales_child_loan_user_list['save_user'] = "Button"
    Sales_child_loan_user_list['save_user'] = "Button"

#********************************Config********************************
class Config:
    Config_ID_Label_list = {}
    Config_ID_Label_list['blacklist_cat_tab'] = "Blacklist Category"
    Config_ID_Label_list['blacklist_num_tab'] = "BlackList Number"
    Config_ID_Label_list['whitelist_cat_tab'] = "Whitelist Category"
    Config_ID_Label_list['whitelist_num_tab'] = "Whitelist Number"

#****************************Config_blacklist_category*********************************
class Config_blacklist_cat:
    Config_blacklist_cat_list = {}
    Config_blacklist_cat_list["//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[1]/input"] = "Police"
    Config_blacklist_cat_list["//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[3]/input"] = "Do not send sms to police"

#***********************Config_ADD_Black_List_Number**********************************************
class Config_ADD_Black_List_Number:
    Config_ADD_Black_List_Number_list = {}
    Config_ADD_Black_List_Number_list['add_blacklist'] = "Add Blacklist Number"
    Config_ADD_Black_List_Number_list['update_blacklist'] = "Upload Blacklist Number"
    Config_ADD_Black_List_Number_list['download_blacklist'] = "Download Blacklist Number"
    Config_ADD_Black_List_Number_list['black_name'] = "Name"
    Config_ADD_Black_List_Number_list['black_desc'] = "Description"
    Config_ADD_Black_List_Number_list['black_number'] = "Number"
    Config_ADD_Black_List_Number_list['add'] = "button"

class Config_ADD_Black_List_Number_dropdown:
    Config_ADD_Black_List_Number_dropdown_list = {}
    Config_ADD_Black_List_Number_dropdown_list['black_category'] = "Police"
    Config_ADD_Black_List_Number_dropdown_list['black_category'] = "Police"

#*******************************Config_ADD_Black_List_Number_input_list************************
class Config_ADD_Black_List_Number_input:
    Config_ADD_Black_List_Number_input_list = {}
    Config_ADD_Black_List_Number_input_list['black_name'] = "Jaykant Shikre"
    Config_ADD_Black_List_Number_input_list['black_desc'] = "Ata Majhi Satakli"
    Config_ADD_Black_List_Number_input_list['black_number'] = "99999999999"


#***************************Config White List Category*************************
class Config_WhiteList_cat:
    Config_WhiteList_cat_list = {}
    Config_WhiteList_cat_list["//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[1]/input"] = "HDFC Customers"
    Config_WhiteList_cat_list["//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[3]/textarea"] = "SMS for Credit Card"

#***********************Config_White_List_Number**********************************************
class Config_White_List_Number:
    Config_White_List_Number_list = {}
    Config_White_List_Number_list['add_whitelist'] = "Add Whitelist Number"
    Config_White_List_Number_list['update_whitelist'] = "Upload Whitelist Number"
    Config_White_List_Number_list['download_whitelist'] = "Download Whitelist Number"
    Config_White_List_Number_list['white_name'] = "Name"
    Config_White_List_Number_list['white_desc'] = "Description"
    Config_White_List_Number_list['white_number'] = "Number"
    Config_White_List_Number_list['add'] = "button"

class Config_White_List_Number_dropdown:
    Config_White_List_Number_dropdown_list = {}
    Config_White_List_Number_dropdown_list['white_category'] = "HDFC Customers"
    Config_White_List_Number_dropdown_list['white_category'] = "HDFC Customers"


#***********************Config_White_List_Number Input**********************************************
class Config_White_List_Number_input:
    Config_White_List_Number_input_list = {}
    Config_White_List_Number_input_list['white_name'] = "Ali"
    Config_White_List_Number_input_list['white_desc'] = "Here Is Awesome Offers HDFC Credit CARD "
    Config_White_List_Number_input_list['white_number'] = "888888888888"

class Config_White_List_Number_dropdown_input:
    Config_White_List_Number_dropdown_input_list = {}
    Config_White_List_Number_dropdown_input_list['white_category'] = "HDFC Customers"
    Config_White_List_Number_dropdown_input_list['white_category'] = "HDFC Customers"

class phonebook_group_edit:
    phonebook_group_edit_inputbox_list = {}
    phonebook_group_edit_inputbox_list["//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/input"] = "abcd"
    phonebook_group_edit_inputbox_list["//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/textarea"] = "wxyz"


class phonebook_contact_edit:
    phonebook_contact_edit_inputbox_list = {}
    phonebook_contact_edit_inputbox_list["//*[@id='addcontact']/div/div/div[2]/div[1]/div[1]/input"] = "william"

################# Campaign #############################
class campaign_edit:
    campaign_edit_inputbox_list = {}
    campaign_edit_inputbox_list["//*[@id='myModal']/div/div/div[2]/div[1]/input"] = "SIGGY"
    campaign_edit_inputbox_list["//*[@id='myModal']/div/div/div[2]/div[2]/textarea"] = "Food Deleivery"