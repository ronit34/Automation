Feature: Hub smppc bind check

    Scenario:  hub smppc bind
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on hub
        And click on SMPPC
        And check bind Button is present
        And Click on bind Button any of createt SMPPC
        And check bind is succussful or not

        And Close driver window