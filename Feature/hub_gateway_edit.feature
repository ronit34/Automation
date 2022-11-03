Feature: Hub Gateway edit

    Scenario: hub gateway edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on hub
        And check edit option is present
        And check delete option is present

         And check edit icon mouse hover text - gateway
        And click on edit option to change info
        And click on the update to save changes

        And Close driver window