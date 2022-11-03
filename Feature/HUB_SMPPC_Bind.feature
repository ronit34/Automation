Feature: HUB SMPPC Bind

    Scenario: Bind in Hub Smppc
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Click on hub
        And click on SMPPC

        And Click on Edit button in Action to enter details
        And Select Carrier name as Airtel
        And Select Vendor name as Airtel
        And Select Circle name as Haryana in SMPPC
        And Enter Primary Host/IP
        And Enter Port Number
        And Select SMPP Bind Type
        And Click on update button to update bind data
        And Click on Bind button for bind
        And Close driver window
