Feature: TUC_New_sms_quick_sms_using_recipient_scrub_DND_send_sms_and_verify_credits

    Scenario: TUC_New_sms_quick_sms_using_recipient_scrub_DND_send_sms_and_verify_credits
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on new SMS
        And Click on Quick English SMS
        And select campaign_name and sender_id
        And Click on Recipient
        And Insert template
        And Check Scrub DND
        And Available credits
        And Click on send button
        And Verify credits according to all number wise deduct or not in quick english sms
        And Close driver window