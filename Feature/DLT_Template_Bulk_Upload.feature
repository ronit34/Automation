Feature: DLT Bulk Upload

    Scenario: DLT Bulk Upload Files
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        Then Click on Bulk Upload
        Then Select Entity Id
        Then Select operator
        Then Choose File
        And  Check for Remove file button
        Then Click on reset
        Then Select Entity Id
        Then Select operator
        Then Choose File
        Then Click on save template
        Then Click on ok butn

        And Close driver window
