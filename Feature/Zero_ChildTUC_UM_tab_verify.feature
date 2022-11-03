Feature: Zero Child TUC User Mgmt tab verify

    Scenario: User Mgmt tab verify in TUC with Zero Child TUC
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "loan" and password "loan"
#        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Check User Mgmt tab is present or not
        And Close driver window
