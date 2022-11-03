Feature: check tenant dashboard label

    Scenario: Tenant_Dashboard_Label_check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Click on User_Management
        And Click on action button to enable account
        And click on action button to disable account
        And click on other reason
        And enter reason for disable
        And click on suspend now
        And mouse hover on disable and verify reason for disable
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "HDFCAdmin" and password "ali"
        And Click on Sign in Button

        And check the error label

        And Close driver window