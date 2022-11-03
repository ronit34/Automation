Feature: SA_Um_Add TA_fill_char_in_licenses_check_error_labels

    Scenario: SA_Um_Add TA_fill_char_in_licenses_check_error_labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Click on User_Management
        And Check Add tenant button present
        Then Click on Add Tenants button
        And check all element present
        And insert detail
        And click create
        Then Check Licenses labels are error or not
        And Close driver window