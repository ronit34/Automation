Feature: Config

    Scenario: Config ids and labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check Config is present
        Then click on Config
        And check Config element is present
        And check Config label is present

        And Close driver window