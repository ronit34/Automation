Feature: Credit Add input

    Scenario: Credit Add input to fields
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on credit allocation
        And click on update credit
        And Select TUC
        And Select Add-Credit
        And Enter the Amount "200000"
        Then Click on update for transaction
        And check credit added successfully

        And Close driver window