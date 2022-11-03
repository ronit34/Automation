Feature: Not Successful Login

    Scenario: Invalid Login Onextel home page
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "onexsa" and password "onexa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Check the message invalid login

        And Close driver window

