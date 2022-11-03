Feature: Quick SMS Short Url

    Scenario: quick short url
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms button
        And click on  Quick English SMS
        And select sender id
        And Insert Template
        And Insert URL
        And click on SEND butn
        And check change in credits after sms is sent "1"

        And Close driver window

