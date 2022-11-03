Feature: phonebook group

    Scenario: group
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on phonebook
        And click on Add group
        And check add group element is present in phonebook
        And insert add group element in phonebook

        And Close driver window
