Feature: Config White List Category

    Scenario:  check Config White List Category
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
        And check all elements of White list category is present
        And insert White list category data
        And click on add button of the given page of White list

        And Close driver window