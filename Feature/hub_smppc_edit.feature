Feature: Hub smppc edit

    Scenario:  hub smppc edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on hub
        And click on SMPPC
        And check edit option is present in SMPPC
        And check delete option is present in SMPPC
         And check edit icon mouse hover text - smppc
        And click on edit option to change info in SMPPC
        And click on the update to save changes in SMPPC

        And Close driver window