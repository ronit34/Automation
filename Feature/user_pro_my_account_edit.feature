Feature: User profile my account edit

    Scenario: edit my account
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on dropdown of super admin onextel
        And click on my account
        And Edit the my account details
        And click on save changes for saving details

        And Close driver window