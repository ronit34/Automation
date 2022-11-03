Feature: Hub smppc

    Scenario: Add hub smppc details
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on hub
        And click on SMPPC
        And click on add smppc
        And check all the element is present
        And insert all the details
        And click on the create button to save smppc details

        And Close driver window