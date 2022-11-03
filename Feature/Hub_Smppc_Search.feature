Feature: Hub smppc search by name

    Scenario: hub gateway edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on hub
        And click on SMPPC
        And search by name
        And search by systemid

        And Close driver window