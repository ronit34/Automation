Feature: phonebook

    Scenario: phonebook ids and labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check phonebook is present
        Then click on phonebook
        And check phonebook element is present
        And check phonebook label is present

        And Close driver window