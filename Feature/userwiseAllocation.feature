Feature: Credit Allocation Userwise

    Scenario: Userwise Allocation
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on credit allocation
        And click on TUC List
        Then click on search

        And Close driver window