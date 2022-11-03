Feature: DLT Entity ID

    Scenario: DLT Entity ids and labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Click on Sign in Button

        Then click on DLT
        And Click on Add Entity button

        And insert values in entity fields
        And click on add button to add entity
        And check edit icon mouse hover text - entityID
        And click on edit icon
        And update values in entity fields
        And click on update
        And check the updated entity id

        And Close driver window
