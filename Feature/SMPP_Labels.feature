Feature: SMPP

    Scenario: SMPP IDs and Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check SMPP is present
        And click on SMPP
        And check element is present on SMPP page
        And check labels are present on SMPP page

        And Close driver window