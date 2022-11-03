Feature: Quick SMS Schedule using Group

    Scenario: quick sms schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Click on Sign in Button

        And click on new sms
        And click on  Quick English SMS
        And insert long temp data into quick sms
        And select new group1
        And Schedule sms

        And click on SEND butn
        And check allow multipart text for long sms
        And check change in credits after schedule "104"

        And click on View Schedule
        And check the scheduled sms is present or not

        And Close driver window