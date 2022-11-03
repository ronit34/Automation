Feature: quick group long

    Scenario: quick group long
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And click on new sms
        And click on quick sms
        And insert long data into quick sms without recipients
        And select test group
        And click on SEND butn
        And check allow multipart text for long sms
        And check change in credits after sms is sent "88"

        And Close driver window

