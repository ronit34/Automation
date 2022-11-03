Feature: After Tenant User Login

    Scenario: successful Login
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And Click on User Button
        And click on add user
        Then insert element
        And click on Create
        And check manger is created or not
        And Close driver window
