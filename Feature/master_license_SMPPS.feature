Feature: Master License SMPPS

    Scenario: Master License SMPPS IDs
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on master license
        And click SMPPS Update button
        And Check the element present on the page
        And enter value "1100"
        Then click on add button of SMPPS

        And Close driver window