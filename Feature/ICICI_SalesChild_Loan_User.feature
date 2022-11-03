Feature: TUC sales Child credit user

    Scenario: credit user
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "sales" and password "sales"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And Click on User Button
        And Click on add User Button
        And check the element is present in sales tuc in user tab
        And enter the data into given field in sales tuc in user tab
        And check tuc user credit is created successfully or not

        And Close driver window