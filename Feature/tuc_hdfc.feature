Feature: Tuc Info HDFC

    Scenario: :
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And Click on Add Tenant Button
        And check elements are present
        And HDFC insert elements

        And Close driver window