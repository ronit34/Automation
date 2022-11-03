Feature: DLT_charge_type_on_delivery

    Scenario: : Account on delivery
        ##### Creating TUC #####
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Telspiel" and password "ali"
        And Click on Sign in Button
        And Click on User_Management
        And Click on Add Tenant Button
        And insert elements into given fields to add tuc
        And click on create button to save it
        ### Creating User #####
        And Click on User Button
        And Click on add User Button
        And insert the data into given fields to add user
        And Log out from the Tenant
        ### Loging in with User and Creating Child #####
        Then Enter Username "AxisUser" and password "ali"
        And Click on Sign in Button
        And Click on User_Management
        And Click on Add Tenant Button

        And Check for OTP charge type option
        And Check for Trans charge type option
        And Check for Promo charge type option
        And Check for Govt charge type option
        And Check for SIM Route charge type option
        And Check for Default charge type option

        And Close driver window