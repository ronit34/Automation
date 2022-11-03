Feature: TUC_new_sms_unicode_sms_using_group_scrub_DND_send_sms_and_verify_credits

    Scenario: TUC_new_sms_unicode_sms_using_group_scrub_DND_send_sms_and_verify_credits
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on Phonebook and create a group and add DND contact
        And Click on new SMS
        And Click on Quick Unicode SMS
        And select campaign_name and sender_id
        And Click on Select group
        And Insert template in unicode
        And Check Scrub DND
        And Check Allow Unicode
        And Available credits
        And Click on send button
        And Verify credits according to all number wise deduct or not in quick english sms
        And Close driver window