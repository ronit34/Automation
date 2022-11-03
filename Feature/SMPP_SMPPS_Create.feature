Feature: SMPP SMPPS

    Scenario: SMPPS
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check SMPP is present
        And click on SMPP
        And click on add SMPPS button
        And check all elements are present in SMPPS
        And insert data into SMPPS field
        And click on create button to create SMPPS

        And Close driver window