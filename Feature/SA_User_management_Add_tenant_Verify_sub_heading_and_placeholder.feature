Feature: SA_User_management_Add_tenant_Verify_sub_heading_and_placeholder

    Scenario: SA_User_management_Add_tenant_Verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Click on User_Management
        And Click on Tenants
        And Click on Add Tenants button
        And Verify Sub_heading and placeholder create_tenant
        And Close driver window
