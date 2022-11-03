Feature: Config ADD Black List Number Input

    Scenario:  Config add Black List num input
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Config
        And click on Black List Number
        And insert data on the given page
        And click on add button of the given page of blni

        And Close driver window