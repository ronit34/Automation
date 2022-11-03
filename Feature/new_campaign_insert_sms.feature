Feature: New Campaign Insert SMS

    Scenario: Campaign Insert SMS
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms
        And click on campaign sms
        And check select file is present
#        And click on select file
#        And Insert Elements on campaign sms
        And click on send button of campaign sms

        And Close driver window