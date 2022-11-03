Feature: User profile change password edit

    Scenario: edit change password
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on dropdown of super admin onextel
        And click on change password
        And Edit password
        And click on submit request button
        And click on log out button to verify change password

        And Close driver window
