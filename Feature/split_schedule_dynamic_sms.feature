  Feature: split schedule dynamic sms

    Scenario: split schedule in dynamic
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

      ###################################################################
        And click on new sms
        And click on new sms
        And click on Dynamic sms
        And select sender Id and campaign
        And Choose variable File
        And insert values in fields
        And click on schedule sms check box
        And click on split schedule sms

        And enter number of splits

        And click on send of dynamic
        And check change in credits after splitting short sms "10"

        And Close driver window





