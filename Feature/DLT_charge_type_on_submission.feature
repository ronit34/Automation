Feature: DLT_charge_type_on_submission

    Scenario: : Account on submission
        ##### Creating TUC #####
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Telspiel" and password "ali"
        And Click on Sign in Button
        And Click on User_Management
        And Click on Add Tenant Button
        And insert elements into given fields
        And click on create button to save it
        #### Creating User #####
        And Click on User Button
        And Click on add User Button
        And insert the data into given fields
        And Log out from the Tenant
        ### Loging in with User and Creating Child #####
        Then Enter Username "SBIUser" and password "ali"
        And Click on Sign in Button
        And Click on User_Management
        And Click on Add Tenant Button

        And Check for OTP charge type option in child
        And Check for Trans charge type option in child
        And Check for Promo charge type option in child
        And Check for Govt charge type option in child
        And Check for SIM Route charge type option in child
        And Check for Default charge type option in child

        And Close driver window