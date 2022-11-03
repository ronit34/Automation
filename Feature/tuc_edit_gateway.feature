Feature: Tuc edit gateway

    Scenario: :
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And check tuc edit option is present
        And check tuc delete option is present
        And check edit icon mouse hover text - gateway edit
        And click on tuc edit option to change info
        And edit the default gateway as per requirements
        And click on the tuc update button to save changes

        And Close driver window


