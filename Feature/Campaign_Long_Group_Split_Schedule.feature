 Feature: campaign long group split schedule

    Scenario: split schedule campaign
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And click on new sms
        And click on campaign sms

        And select sender Id and campaign
        And select test group for dynamic
        And insert data

        And click on schedule sms check box
        And click on split schedule to split

        And click on send
        And check change in credits after splitting long sms "88"
        And Close driver window

