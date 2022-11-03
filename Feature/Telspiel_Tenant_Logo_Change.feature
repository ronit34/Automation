Feature: Telspiel Tenant logo change feature

    Scenario: logo_change
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Telspiel" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then click on dropdown of super admin onextel
        And click on my account
        And Select logo
        And Select icon
        And Select login page logo
        And click on save changes button
        And click on ok button

        And Close driver window