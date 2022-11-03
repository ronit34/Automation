Feature: Clear Calendar date in report summary

    Scenario: Clear Calendar date in report summary
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on Report
        And Click on Summary
        And Clear From date
        And Click on Summary search button
        And Verify data available
        And Close driver window