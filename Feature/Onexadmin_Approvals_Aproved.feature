Feature: Onexadmin Approvals Approved Permission

    Scenario: Approved Permission
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click On Approvals
#        And click on approved button
        And click on Approved tab to check status

        And Close driver window