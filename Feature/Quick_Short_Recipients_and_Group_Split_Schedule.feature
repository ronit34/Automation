Feature: split schedule quick short sms

    Scenario: split schedule short sms
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on quick sms
        And select sender id
        And select group
        And insert short template data
        And click on schedule sms
        And click on split schedule with different time

        And click on send of short recipient split schedule
        And check change in credits after splitting short sms "23"

        And Close driver window
