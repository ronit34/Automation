Feature: Onextel Tenant User Management
  Scenario: Login to Onextel Tenant Dashboard

        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button

        Then click on User_Management
        And Click on Search btn in UserMgmt
        And Select TUCID in UserMgmt
        And Enter TUCID
        And Click Search

        And Check for TUC Hierarchy
        And Check for Name in UserMgmt
        And Check for Credits
        And Check for Bill Type
        And Check for DLT Charge
        And Check for SMS Charge

        And Close driver window


