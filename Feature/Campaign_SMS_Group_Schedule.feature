Feature: Campaign SMS Schedule using Group

    Scenario: campaign sms schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Click on Sign in Button
        And click on new sms
        And click on campaign sms
        And select campaign name and sender id
        And select new group for campaign
        And Insert Template
        And Schedule sms
        And click on send button
        And click on send now button of dynamic sms
        And click on View Schedule

        And Close driver window
