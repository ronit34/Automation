Feature: Schedule campaign SMS for file upload and select group

    Scenario: Campaign Schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on campaign sms

        And Choose new File for campaign sms
        And select a sender id
        And select test group for dynamic
        And Insert Template
        And Schedule sms
        And click on send button
        And click on send now button of campaign sms
#        And click on View Schedule
#        And check the scheduled sms is present
        And Close driver window