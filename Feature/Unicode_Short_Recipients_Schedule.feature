Feature: View Schedule unicode SMS

    Scenario: View Schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on Quick Unicode/Multilingual SMS

        And select new sender id
        And insert unicode data
        And click on allow unicode
        And Schedule sms

        And click on send button
        And click on send now button of dynamic sms

        And click on View Schedule
        And check the scheduled sms is present

        And Close driver window