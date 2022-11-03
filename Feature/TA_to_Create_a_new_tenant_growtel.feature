Feature: Create a tenant(Growtel)

  Scenario: Create a tenant(Growtel)
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "onexsa" and password "onexsa"
        And Click on Sign in Button
        Then click on User_Management
        And Click on Add Tenant
        And Insert details of growtel
        And Click on create tenant
        And Click on User
        And Click on Add User
        And Insert details for growtel
        And Close driver window
