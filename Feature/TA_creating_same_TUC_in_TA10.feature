Feature: SA_Creating_TA_with_same_name

    Scenario: SA_Creating_TA_with_same_name
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on User management
        And Click on Add TUC in TA10
        And Insert details in add TUC in TA10 for same name
        And Click on create in add TUC in TA10
        And Verify tenant create or not in TA10
        And Close window driver