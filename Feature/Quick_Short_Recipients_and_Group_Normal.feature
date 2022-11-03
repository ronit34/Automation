Feature: View Schedule Quick SMS

    Scenario: View Schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And click on new sms
        And click on quick sms
        And insert short data into quick sms
        And select test group
        And click on SEND butn
        And check change in credits after sms is sent "26"

        And Close driver window