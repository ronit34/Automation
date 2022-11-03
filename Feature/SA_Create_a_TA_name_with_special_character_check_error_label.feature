Feature: SA_Create_a_TA_name_with_special_character_check_error_label

    Scenario: SA_Create_a_TA_name_with_special_character_check_error_label
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Click on User_Management
        Then Click on Add Tenants button
        And check all element present
        And Insert details with special element
        And click create
        And Check error label for special character
        And Close driver window