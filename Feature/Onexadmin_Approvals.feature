Feature: Onexadmin Approvals

    Scenario: Approvals
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check approvals is present
        And Click On Approvals
        And Check all tabs are there
        And check all labels of tabs are there

        And Close driver window
