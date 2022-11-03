Feature: SA_create_tenant_user_logout_TA_login_verify_logout_SA_login_user_idpass_login_verify

    Scenario: SA_create_tenant_user_logout_TA_login_verify_logout_SA_login_user_idpass_login_verify
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Click on User_Management
        Then Click on Add Tenants button
        And check all element present
        And insert detail for create tenant
        And click create
        And Click on user in user_management

        And Click on Add User

        And Insert details in user info
        And Click on create in user info
        And Logout from SA

        Then Enter Username "ronitqwerty" and password "qwerty@123"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Verify TA login or not
        And Logout from TA

        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Click on User_Management
        And Click on user in user_management
        And Click on edit button in user_TA
        And Insert new id and password in user info
        And Click on update button in user info
        And Logout from TA

        Then Enter Username "ron" and password "pat"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Verify TUC login or not

        And Close driver window