Feature: Quick SMS long group Url

    Scenario: quick long group url
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms button
        And click on  Quick English SMS
        And select sender id for group
        And select test group

        And Insert Long Template
        And Insert URL in Long template
        And select the Allow Multi Part SMS checkbox
        And check change in credits for long url after sms is sent "88"

        And Close driver window