Feature: DLT Entity ID

    Scenario: DLT Entity ids and labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        And check delete icon mouse hover text - entityID
        And click on delete icon against entityID
        And check error label in popup
        And click on Delete Button to delete EntityID

        And Close driver window