Feature: Config White List Number Input

    Scenario:  check Config White List num input
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Config
        And click on white list number
        And insert data on the given page of white list number
        And click on add button of the given page of white list number

        And Close driver window