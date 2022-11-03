Feature: Check TUC Credit In Tenant

    Scenario: TUC Credit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Check TUC select dropdown is present
        And Select tuc for showing records

        And Close driver window
