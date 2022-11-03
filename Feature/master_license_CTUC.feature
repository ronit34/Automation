Feature: Master License CTUC

    Scenario: Master License CTUC IDs
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on master license
        And click on CTUC Update button
        And Check CTUC elements are present
        And enter value to update CTUC "1100"
        Then click on add button

        And Close driver window