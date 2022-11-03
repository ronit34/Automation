Feature: TUC_Campaign_SMS_character_length_and_verify_credits

    Scenario: TUC_Campaign_SMS_character_length_and_verify_credits
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And click on new sms
        And click on campaign sms
        And select campaign_name and sender_id
        And select new_group for campaign
        And Insert Template
        And Count character and credits

        And Close driver window