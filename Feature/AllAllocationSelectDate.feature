Feature: All Allocation Date Selection

    Scenario: All Allocation date select
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on credit allocation
        Then click on all allocation
        And select from date "21112021"
        And select to date "22112021"
        Then click on search button
        And Close driver window