Feature: New SMS Dynamic Input

    Scenario: dynamic insert data
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#       Then Check if the message invalid login then close the browser
        And click on new sms
        And click on Dynamic sms
        And insert data into Dynamic sms
        And click on send button
        And click on send now button of dynamic

        And Close driver window