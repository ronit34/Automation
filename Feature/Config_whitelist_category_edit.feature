Feature: Config WhiteList Category Edit

    Scenario: Config WhiteList Category edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Config
        And click on White List Category
        And check new Whitelist button is present
        And click on new Whitelist button
        And insert whitelist data
        And click on add button of the given page of White list

        And check edit icon mouse hover text - whitelist

        And Click on Edit of the created whitelist category
        And Enter new whitelist category name to update
        And Enter new category description to update
        And Click on update button to update whitelist data

        And Close driver window
