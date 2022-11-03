Feature: split schedule quick unicode sms

    Scenario: unicode split schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And click on new sms
        And click on Quick Unicode/Multilingual SMS
        And select new sender id
        And insert unicode data
        And click on schedule sms
        And click on split schedule and insert different time

        And click on send button of unicode
        And check change in credits after splitting short sms "4"

        And Close driver window

