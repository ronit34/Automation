Feature: New SMS Quick Insert Template

    Scenario: Insert Template
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms
        And click on quick sms
        And select sender Id
        And click on Insert Template
        And Check elements are present in popup window

        And Close driver window