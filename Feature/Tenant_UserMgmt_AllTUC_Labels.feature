Feature: Onextel Tenant User Management
  Scenario: Login to Onextel Tenant Dashboard

        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button

        Then click on User_Management
        And Click on All TUC
        And Check for TUC Name in All TUC
        And Check for ChildTUC1 in All TUC
        And Check for ChildTUC2 in All TUC
        And Check for Credit

        And Close driver window
