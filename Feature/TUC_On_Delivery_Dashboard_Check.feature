Feature: TUC On Delivery Dashboard Check

    Scenario: : Dashboard Check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "AxisUser" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And Check for Delivered Percent text in Pie Chart
        And Close driver window
