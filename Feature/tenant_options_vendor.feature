Feature: Tenant Options Vendor

    Scenario: Vendor
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on Options button
        And Click on vendor tab
        And Click on Add vendor
        And Check elements are present in vendor
        And enter data into vendor
        And click on add button of Options to add entered data
        And Verify vendor is added or not

        And Close driver window