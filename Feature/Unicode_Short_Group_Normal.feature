Feature: New SMS Unicode Input short group

    Scenario: Unicode short recipients SMS
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on Unicode sms
        And insert data into Unicode sms without recipients
        And select test group
        And click on send now button "44"

        And Close driver window