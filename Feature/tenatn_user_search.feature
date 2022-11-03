Feature: search user

    Scenario: : searching a user using the search box
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on User_Management
        And Click on User Button
        And check error label of user search

        And Close driver window