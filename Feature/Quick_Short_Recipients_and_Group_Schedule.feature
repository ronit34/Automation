Feature: Quick SMS Schedule using Group

    Scenario: quick sms schedule
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Click on Sign in Button

        And click on new sms
        And click on  Quick English SMS
        And select new group1
        And insert short temp data into quick sms
        And Schedule sms

        And click on SEND butn
        And check change in credits after schedule "26"

        And click on View Schedule
        And check the scheduled sms is present or not

        And Close driver window