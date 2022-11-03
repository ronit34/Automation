Feature: split schedule quick short sms

    Scenario: split schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And click on new sms
        And click on quick sms
        And select sender_id
        And select group
        And insert short template data
        And click on schedule sms
        And click on split schedule to split with different time

        And click on send of short recipient split schedule
        And check change in credits after splitting short sms "22"

        And Close driver window