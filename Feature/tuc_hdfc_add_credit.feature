Feature: tuc HDFC credit Add input

    Scenario: HDFC add credit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on credit allocation
        And click on update credit
        And Select TUC as HDFC
        And Select Add-Credit for HDFC
        And Enter the Amount "2000"
        Then Click on update for transaction
        And check updated credit is showing or not

        And Close driver window