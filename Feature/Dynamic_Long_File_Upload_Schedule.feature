Feature: Dynamic Long file upload schedule

    Scenario: View Schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on Dynamic sms
        And select sender Id and campaign
        And Choose variable File
        And insert long template data for dynamic

        And Schedule dynamic sms
        And Click on Allow MultiPart SMS
        And click on send button
        And click on send now button of dynamic sms
        And click on View Schedule
        And check the scheduled sms is present

        And Close driver window