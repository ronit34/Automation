Feature: split schedule unicode short sms

    Scenario: split schedule short sms
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on Quick Unicode/Multilingual SMS
        And select sender id
        And select group
        And insert unicode data
        And click on schedule sms
        And click on split schedule with different time

        And click on send button of unicode
        And check change in credits after splitting short sms "23"

        And Close driver window
