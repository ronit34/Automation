Feature: Tenant Spam Labels

    Scenario: Spam Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Click on Sign in Button

        And Click on Spam
        And Click on Category Assign tab
        And Click on Add TUCs

        And Select Category from Dropdown
        And select the Tucs from the tuc list
        And Click Add

        And Select Category from Dropdown
        And Click On Search and check assigned category

        And Close driver window
