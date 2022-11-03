Feature: TUC_new_sms_multiple_dynamic_sms_send_sms_verify_credits

    Scenario: TUC_new_sms_multiple_dynamic_sms_send_sms_verify_credits
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And click on new sms
        And Click on Multiple Dynamic SMS
        And Click on choose file for multiple dynamic sms
        And select campaign_name and sender_id
