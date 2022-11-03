Feature: TUC ICICI Child user sales

    Scenario: TUC_ICICI_Child_user sales
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And Click on User Button
        And Click on add User Button
        And check the element is present in icici tuc
        And enter the data into given field in icici tuc
        And check tuc user sales is created suucessfully or not

        And Close driver window