Feature: View Schedule Quick SMS

    Scenario: View Schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And click on new sms
        And click on quick sms
        And insert long temp data into quick sms
        And Schedule sms

        And click on SEND butn
        And check allow multipart text for long sms
        And check change in credits after schedule "16"

        And click on View Schedule
        And check the scheduled sms is present

        And Close driver window
