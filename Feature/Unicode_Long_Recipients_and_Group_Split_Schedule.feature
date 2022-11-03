Feature: split schedule unicode sms

    Scenario: split schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And click on new sms
        And click on Quick Unicode/Multilingual SMS
        And select sender id
        And select group
        And insert unicode long template data
        And click on schedule sms
        And click on split schedule

        And click on send button of unicode
        And check change in credits after splitting long sms "161"

        And Close driver window