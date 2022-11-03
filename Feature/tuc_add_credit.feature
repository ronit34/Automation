Feature: tuc credit Add input

    Scenario: tuc add credit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on credit allocation
        And click on update credit
        And Select TUC as ICICI
        And Select Add-Credit
        And Enter the Amount "25000"
        Then Click on update for transaction of tuc
        And check credit alloted successuflly

        And Close driver window