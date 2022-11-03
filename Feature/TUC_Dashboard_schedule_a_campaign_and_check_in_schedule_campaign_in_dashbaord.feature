Feature: TUC_Dashboard_schedule a campaign and check in schedule campaign in dashbaord

    Scenario: TUC_Dashboard_schedule a campaign and check in schedule campaign in dashbaord
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
        And Schedule sms
        And click on send button

        And Click on Send NOW_Button
        Then Click on Dashboard
        And Click on Dashboard Scheduled SMS
        And Check seheduled sms is present or not

        And Close driver window

