Feature: Hub Gateway

    Scenario: Add hub gateway details
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on hub
        And click on add gateway
        And check element present
        And insert the element
        And click on the create

        And Close driver window