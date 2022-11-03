Feature: Master License  SMS API

    Scenario: Master License  SMS API  IDs
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on master license
        And click on the SMS API Update button
        And Check the element present on the page
        And enter value "1200"
        Then click on add button of SMS API

        And Close driver window