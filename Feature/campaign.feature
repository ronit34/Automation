Feature: create campaign

    Scenario: : Common steps
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Check Campaign is present
        Then click on Campaign
        And check campaign element is present
        And check campaign label is present

        And Close driver window
