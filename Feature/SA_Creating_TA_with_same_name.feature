Feature: SA_Creating_TA_with_same_name

    Scenario: SA_Creating_TA_with_same_name
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on User management
        And Click on Add tenant in SA
        And Insert details in add tenant in SA for same name
        And Click on create in add tenant in SA
        And Verify tenant create or not in SA
        And Close window driver