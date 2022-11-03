Feature: Master Balance Add

    Scenario: Master Update Balance
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on master balance
        And click on the Update Balance
        And Enter amount "100000"
        And click on the add button

        And Close driver window
