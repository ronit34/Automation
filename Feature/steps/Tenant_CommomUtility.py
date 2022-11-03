from datetime import datetime
import calendar
x = datetime.now()
current_Day_Date = (x.strftime("%A" " " "%d" " " "%B" " " "%Y"))

# *************************** Telspiel Tenant *************************************************
class tenant_telspiel_creator:
    tenant_telspiel_creator_inputbox_list = {}
    tenant_telspiel_creator_inputbox_list['name'] = "Telspiel"
    tenant_telspiel_creator_inputbox_list['description'] = "Its a company"
    tenant_telspiel_creator_inputbox_list['childtuc'] = "100"
    tenant_telspiel_creator_inputbox_list['smpps'] = "100"
    tenant_telspiel_creator_inputbox_list['smsapi'] = "100"
    # tenant_creator_inputbox_list['smsapi_tenant'] = "8"
    tenant_telspiel_creator_inputbox_list['cancel'] = "Button"
    tenant_telspiel_creator_inputbox_list['save_tenant'] = "Button"
    tenant_telspiel_creator_inputbox_list['save_tenant'] = "Button"

class telspiel_user_creator:
    telspiel_user_creator_inputbox_list = {}
    telspiel_user_creator_inputbox_list['username'] = "Telspiel"
    telspiel_user_creator_inputbox_list['password'] = "ali"
    telspiel_user_creator_inputbox_list['fname'] = "Telspiel"
    telspiel_user_creator_inputbox_list['lname'] = "Telspiel"
    telspiel_user_creator_inputbox_list['email'] = "onex@"
    telspiel_user_creator_inputbox_list['mob_no'] = "8"
    telspiel_user_creator_inputbox_list['comp_name'] = "OneX"
    telspiel_user_creator_inputbox_list['web'] = "onextel.tech"
    telspiel_user_creator_inputbox_list['other_mob_no'] = "3"
    telspiel_user_creator_inputbox_list['cancel'] = "Button"
    telspiel_user_creator_inputbox_list['save_user'] = "Button"
    telspiel_user_creator_inputbox_list['save_user'] = "Button"
class telspiel_user_creator_dropdown:
    telspiel_user_creator_dropdown_inputbox_list = {}
    telspiel_user_creator_dropdown_inputbox_list['role_type'] = "Tenant Admin"
    telspiel_user_creator_dropdown_inputbox_list['tenant'] = "Telspiel"

# 4. ************************* HUB  GATEWAY******************************************************
class hub_gateway:
    hub_gateway_inputbox_list = {}
    hub_gateway_inputbox_list['gateway_name'] = "1"
    hub_gateway_inputbox_list['description'] = "23"

class hub_gateway_dropdown:
    hub_gateway_dropdown_inputbox_list = {}
    hub_gateway_dropdown_inputbox_list['carrier_id'] = "AIRTEL"
    hub_gateway_dropdown_inputbox_list['circle_id'] = "Haryana"
    hub_gateway_dropdown_inputbox_list['circle_id'] = "Haryana"

class hub_gateway_edit:
    hub_gateway_edit_list = {}
    hub_gateway_edit_list['gateway_name'] = "AIRTEL-OTP-1"
    hub_gateway_edit_list['description'] = "OTP MESSAGE"

class hub_gateway_dropdown_edit:
    hub_gateway_dropdown_edit_list = {}
    hub_gateway_dropdown_edit_list['carrier_id'] = "AIRTEL"
    hub_gateway_dropdown_edit_list['circle_id'] = "Haryana"
    hub_gateway_dropdown_edit_list['circle_id'] = "Haryana"


# **********************************HUB SMPPC*************************************************

class hub_smppc:
    hub_smppc_inputbox_list = {}
    hub_smppc_inputbox_list['name'] = "Abc"
    hub_smppc_inputbox_list['smpplogin'] = "23"
    hub_smppc_inputbox_list['username'] = "ab"
    hub_smppc_inputbox_list['password'] = "abc123"
    hub_smppc_inputbox_list['host'] = "abc"
    hub_smppc_inputbox_list['port'] = "8000"
    hub_smppc_inputbox_list['cost'] = "1234"
    hub_smppc_inputbox_list['tps'] = "56789"
    hub_smppc_inputbox_list['num_binds'] = "1"
    hub_smppc_inputbox_list['remarks'] = "This is Updated smppc"

class hub_smppc_dropdown:
    hub_smppc_inputbox_list = {}
    # hub_smppc_inputbox_list['gateway_id'] = "1"
    hub_smppc_inputbox_list['carrier_id'] = "AIRTEL"
    hub_smppc_inputbox_list['circle_id'] = "Haryana"
    hub_smppc_inputbox_list['supports_flash'] = "False"
    hub_smppc_inputbox_list['mode'] = "TRANSCEIVER(TRX)"

#***************************HUB SMPPC EDIT *******************************************
class hub_smppc_edit:
    hub_smppc_edit_list = {}
    hub_smppc_edit_list['name'] = "AIRTEL"
    hub_smppc_edit_list['smpplogin'] = "user1"
    hub_smppc_edit_list['username'] = "user1"
    hub_smppc_edit_list['password'] = "pass1"
    hub_smppc_edit_list['host'] = "127.0.0.1"
    hub_smppc_edit_list['port'] = "5555"
    hub_smppc_edit_list['cost'] = "5"
    hub_smppc_edit_list['tps'] = "100"
    hub_smppc_edit_list['num_binds'] = "2"
    # hub_smppc_edit_list['telemarid'] = "140200000107"

class hub_smppc_dropdown_edit:
    hub_smppc_dropdown_edit_list = {}
    hub_smppc_dropdown_edit_list['gateway_id'] = "AIRTEL-OTP-1"
    hub_smppc_dropdown_edit_list['carrier_id'] = "AIRTEL"
    hub_smppc_dropdown_edit_list['circle_id'] = "Haryana"
    hub_smppc_dropdown_edit_list['supports_flash'] = "False"
    hub_smppc_dropdown_edit_list['mode'] = "TRANSCEIVER(TRX)"

class hub_smppc_bind:
    hub_smppc_bind_list = {}
    hub_smppc_bind_list["//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[7]"] = "1"
    hub_smppc_bind_list["//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]"] = "5555"


#***************************** Hub Smppc Select Fielter ************************
class hub_smppc_dropdown_fill:
    hub_smppc_dropdown_fill_list = {}
    hub_smppc_dropdown_fill_list['carrier'] = "AIRTEL"
    hub_smppc_dropdown_fill_list['vendor'] = "vendor_AIRTEL"
    hub_smppc_dropdown_fill_list['type'] = "OTP"
    hub_smppc_dropdown_fill_list['circle'] = "Haryana"
    hub_smppc_dropdown_fill_list['gateway_id'] = "AIRTEL-P-2"

class hub_smppc_dropdown_fill0:
    hub_smppc_dropdown_fill_list0 = {}
    hub_smppc_dropdown_fill_list0['carrier'] = "AIRTEL"
    hub_smppc_dropdown_fill_list0['vendor'] = "vendor_AIRTEL"
    hub_smppc_dropdown_fill_list0['type'] = "OTP"
    hub_smppc_dropdown_fill_list0['circle'] = "Haryana"
    hub_smppc_dropdown_fill_list0['gateway_id'] = "AIRTEL-OTP-1"

class hub_smppc_dropdown_fill1:
    hub_smppc_dropdown_fill_list1 = {}
    hub_smppc_dropdown_fill_list1['search_name'] = "SKV_MTXT_P3"
    hub_smppc_dropdown_fill_list1['user_id']="Name"

class hub_smppc_dropdown_fill2:
    hub_smppc_dropdown_fill_list2 = {}
    hub_smppc_dropdown_fill_list2['search_name'] = "SKV_MTXT_P3"
    hub_smppc_dropdown_fill_list2['user_id']="system_id"
# 8. ***************** Options *****************************************************
# a)Circle
class options_circle:
    options_circle_list = {}
    options_circle_list['circle_name'] = "Haryana"
    options_circle_list['circle_desc'] = "Sent SMS"
    options_circle_list['add_option'] = "Add"
    options_circle_list['cancel_modal'] = "Cancel"

# b)Carrier
class options_carrier:
    options_carrier_list = {}
    options_carrier_list['carrier_name'] = "AIRTEL"
    options_carrier_list['carrier_desc'] = "Sent SMS Through This Carrier In Haryana Circle"
    options_carrier_list['add_option'] = "Add"
    options_carrier_list['cancel_modal'] = "Cancel"

# c)Type
class options_type:
    options_type_list = {}
    options_type_list['type_atom'] = "otp"
    options_type_list['type_name'] = "OTP"
    options_type_list['type_desc'] = "Its a one time password message"
    options_type_list['add_option'] = "Add"
    options_type_list['cancel_modal'] = "Cancel"

# d)Vendor
class options_Vendor:
    options_Vendor_list = {}
    options_Vendor_list['vendor_name'] = "vendor_AIRTEL"
    options_Vendor_list['vendor_telemar'] = "12345678"
    options_Vendor_list['vendor_desc'] = "Its a AIRTEL Vendor"
    options_Vendor_list['add_option'] = "Add"
    options_Vendor_list['cancel_modal'] = "Cancel"

