Feature: TUC Notification

    Scenario: TUC Notification Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"

        And Click on Sign in Button

        And check Notification is present
        Then click on Notification

        And check if Notification Subject text is present or not
        And check if Notification Content text is present or not
        And check if Notification Applicable To Subject text is present or not
        And check if Notification Created at text is present or not
        And check if Notification Action text is present or not

        And Click on Add Notification

        And Check if Add Notification text is present or not
        And Check if Subject text is present or not in pop up
        And Check if Content text is present or not in pop up
        And Check if Applicable To text is present or not in pop up
        And Check if Add text is present or not in pop up
        And Close driver window















