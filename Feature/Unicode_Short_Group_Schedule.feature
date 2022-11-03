Feature: Unicode SMS Schedule using Group

    Scenario: unicode sms schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Click on Sign in Button

        And click on new sms
        And click on Quick Unicode/Multilingual SMS

        And select sender_id
        And select group
        And insert unicode data

        And click on allow unicode
        And Schedule sms
        And click on send button
        And click on send now button of dynamic sms
        And click on View Schedule
        And check the scheduled sms is present or not in campaign

        And Close driver window