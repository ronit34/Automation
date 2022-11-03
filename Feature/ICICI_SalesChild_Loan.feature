Feature: Create child tuc in sales tuc

    Scenario: tuc sales
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "sales" and password "sales"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And Click on Add Tenant Button
        And check elements are present in add tuc of sales
        And insert elements in add tuc of sales
        And click on create button to save it
        And check tuc is created in sales tuc

        And Close driver window