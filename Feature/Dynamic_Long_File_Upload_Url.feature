Feature: New SMS Dynamic normal group

    Scenario: dynamic normal group
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on Dynamic sms
#        And select test group
        And insert data into Dynamic long for URL
        And Insert URL in Long template dynamic
        And click on send button

        And click on send button check popup

        And Close driver window