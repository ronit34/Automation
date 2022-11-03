Feature: New Campaign SMS

    Scenario: Campaign SMS
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms
        And click on campaign sms
        And check campaign sms elements are present
        And check campaign sms check boxes are present

        And Close driver window