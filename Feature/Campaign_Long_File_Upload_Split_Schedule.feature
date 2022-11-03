 Feature: campaign long file upload split schedule

    Scenario: split schedule campaign
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
        And insert data

        And click on schedule sms check box
        And click on split schedule sms button
        And click on send
        And click on send of short recipient split schedule
        And check change in credits after splitting long sms "16"
        And Close driver window

