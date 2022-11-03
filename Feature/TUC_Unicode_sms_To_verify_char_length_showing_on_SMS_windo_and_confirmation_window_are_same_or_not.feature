Feature: TUC_Quick_sms_To verify char length showing on SMS windo and confirmation window are same or not

    Scenario: TUC_Quick_sms_To verify char length showing on SMS windo and confirmation window are same or not
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And click on new sms
        And click on Unicode sms
        And select campaign_name and sender_id
        And insert data into Unicode_sms
        And Count characters for unicode
        And click on send button
        And Verify char length showing on SMS windo and confirmation window are same or_not

#        And Close driver window