Feature: Master Update super admin Balance

    Scenario: Master Update Balance IDs and Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on master bal
        And click on super admin history
        And click on search of history
        And select from date popup "01032022"
        And select to date popup "02032022"
        Then click on search butn

        And Close driver window