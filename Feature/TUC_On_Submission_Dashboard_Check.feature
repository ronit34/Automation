Feature: TUC On Submission Dashboard Check

    Scenario: : Dashboard Check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "SBIUser" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And Check for Submitted Percent text in Pie Chart
        And Close driver window
