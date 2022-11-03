Feature: DLT senderID

    Scenario: create DLT senderID
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        Then click on DLT
        And click on sender ids tab
        And click on delete icon in SenderID
        And check labels in popup
        And click on Delete Button to delete EntityID

        And Close driver window
