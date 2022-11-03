Feature: New SMS

    Scenario: New SMS
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check new sms is present
        And click on new sms
        And check ALL new sms elements are present

        And Close driver window
