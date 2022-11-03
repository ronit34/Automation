Feature: phonebook add single contact contact

    Scenario: single contact
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on phonebook
        And click on contact
        And click on add contact to create single contact
        And check single contact is present
        And click on single contact
        And elements are present
        And insert data in single contact field
        And click on the Add Button of single contact

        And Close driver window