Feature: TUC_new_sms_Quick_sms_uncheck_remove_duplicate_and_invalid_send_sms_verify_credits

    Scenario: TUC_new_sms_Quick_sms_uncheck_remove_duplicate_and_invalid_send_sms_verify_credits
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on new SMS
        And Click on Quick English SMS
        And select campaign_name and sender_id
        And Click on Recipient
        And Uncheck Remove Invalid Numbers in quick sms
        And Uncheck Remove Duplicate Numbers in quick sms
        And Insert template
        And Available credits
        And Click on send button

        And Verify credits according to all number wise deduct or not in quick english sms
        And Close driver window

