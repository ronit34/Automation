Feature: Dynamic SMS Particular file upload

    Scenario: Dynamic SMS file upload
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on Dynamic sms

        And Choose unicode check File
        And select sender Id and campaign
        And Select Recipient Column
        And Insert Data for Dynamic SMS
        And Click on preview

        And click on send button of dynamic
        And check change in credits after the sms is sent "16219"

        And Close driver window