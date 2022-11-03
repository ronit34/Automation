Feature: Report

    Scenario: Check ID and labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check report is present
        And click on report
        And check ALL report elements are present
        And check ALL report Labels are present

        And Close driver window
