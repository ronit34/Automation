Feature: Hub smppc select fielter

    Scenario: hub gateway edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on hub
        And click on SMPPC
        And Select data
        And select another data
#        And check the data present

        And Close driver window