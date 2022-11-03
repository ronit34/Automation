Feature: TUC_new_sms_Campaign_sms_uncheck_remove_invalid_send_sms_verify_credits

    Scenario: TUC_new_sms_Campaign_sms_uncheck_remove_invalid_send_sms_verify_credits
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on new SMS
        And Click on Campaign SMS
        And Click on choose file in campaign sms
        And select campaign_name and sender_id
        And Uncheck Remove Invalid Numbers
        And Insert template
        And Click on send button
        And Verify credits according to all number wise deduct or not
        And Close driver window