Feature: Master Balance

    Scenario: Master Balance IDs and Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check master balance is present
        And click on master balance
        And check the element should be present
        And discover all related label
        And Close driver window
