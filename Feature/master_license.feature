Feature: Master License

    Scenario: Master License IDs
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Check the Master License is present
        And click on master license
        And check all elements is present in master license page

        And Close driver window