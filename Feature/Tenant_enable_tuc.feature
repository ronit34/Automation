Feature: Tenant Action Button Check

    Scenario: Action Button
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on User_Management
        And check if action button is present on the page for TUC
        And Enable TUC

        And Close driver window
