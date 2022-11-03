Feature: Campaign Long SMS Schedule using Group

    Scenario: campaign sms schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Click on Sign in Button

        And click on new sms
        And click on campaign sms

        And select a sender id
        And select test group for dynamic
        And Insert Long Template
        And Schedule sms
        And click on send button
        And click on send now button of campaign sms
#        And click on View Schedule
        And Close driver window
