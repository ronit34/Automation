Feature: DLT URL Delete

    Scenario: DLT URL Delete
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        And Click on URL
        And check delete icon mouse hover text - URL
        And Click on Delete icon
        And Check Delete Labels
        And Click on Delete button of pop up

        And Close driver window