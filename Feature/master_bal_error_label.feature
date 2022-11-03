Feature: practise

    Scenario: check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on master
        And click on the Update
        Then click on add but
        Then check error lab

        And Close driver window