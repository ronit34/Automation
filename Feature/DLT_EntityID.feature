Feature: DLT Entity ID

    Scenario: DLT Entity ids and labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        And Click on Add Entity button
        And Check DLT Entity element is present
        And Insert data into entity fields
        And click on add button to add entity
        And Check entity id is created or not

        And Close driver window