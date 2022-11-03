Feature: Tenant Options Add Carrier

    Scenario: Add Carrier
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on Options button
        And Click on Carrier tab
        And Click on Add Carrier
        And check text of Add Carrier
        And check text of CarrierName
        And check text of Carrier add Description
        And check text of Carrier Add
        And check on Cancel of add Carrier

        And Close driver window