Feature: After Tenant_Customer Created

    Scenario: Tenant_Customer_User
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And Click on User Button
        And Click on add User Button
        And check the element is present
        And enter the data into given field
        And check tuc user is created successfully or not

        And Close driver window

