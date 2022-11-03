Feature: tenant option type

    Scenario: : Common steps
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on option
        And Click on type
        And Click on add type
        And Click multiple type

        And Close driver window
