Feature: create telspiel user

    Scenario: : user
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on User_Management
        And click on User
        And check Bell Icon present
        And check Date present on the page
        And check add user button
        And click on add user
        Then check all elements are present in tenant user
        And insert input data in tenant login
        And click on create Button
        And check user is created or not of telspiel tenant

        And Close driver window