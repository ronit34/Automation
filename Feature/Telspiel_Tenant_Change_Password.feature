Feature: Telspiel Tenant change password feature

    Scenario: change password
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Telspiel" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then click on dropdown of super admin onextel
        And click on change password
        And Enter details in current ,new and re-enter password fields
        And Click on submit request button
        And Check Successfully changed Password for Telspiel message is displayed
        And Click on ok

        And Close driver window