Feature: Tenant User Management Search User

    Scenario: Search User
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And switch to user
        And search for the user "Sant"
        And click on the search button
        And finally check if the search field is present or not

        And Close driver window