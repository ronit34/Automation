Feature: New SMS Quick

    Scenario: Quick SMS
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms
        And click on quick sms
        And check all elements are present in quick sms
        And check some labels are presents
        And insert data into quick sms
        And click on send button
        And check pop up window is coming

        And Close driver window