Feature: After Login to SuperAdmin Create Tenant

    Scenario: :
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then Click on User_Management
        And Check Add tenant button present
        Then Click on Add Tenants button
        And check all element present
        And insert details
        And click create
        And check Tenant created succussfully or not

        And Close driver window



