Feature: schedule using file and group in campaign sms

    Scenario: schedule campaign
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And click on new sms
        And click on campaign sms

        And Choose new File for campaign sms
        And select sender Id and campaign
        And insert values in campaign fields

        And Schedule sms
        And click on send button
        And Close driver window