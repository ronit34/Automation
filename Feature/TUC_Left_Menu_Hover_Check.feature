Feature: TUC Left Menu Hover Check

    Scenario: TUC Hover Check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on Arrow symbol
        And Hover on Dashboard and check text
        And Hover on Campaign and check text
        And Hover on User Management and check text
        And Hover on Credits and check text
        And Hover on Reports and check text
        And Hover on Telco Reports and check text
        And Hover on DLT and check text
        And Hover on SMPP and check text
        And Hover on API and check text
#        And Hover on Approvals and check text
        And Hover on Phonebook and check text
        And Hover on Config and check text
        And Hover on Notification and check text

        And Close driver window


