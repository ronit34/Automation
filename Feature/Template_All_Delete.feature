Feature: DLT All Template Delete

    Scenario: Delete All Template
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        Then click on template
        And Click on Delete All button
        And Click on Delete button of the pop up

        And Close driver window