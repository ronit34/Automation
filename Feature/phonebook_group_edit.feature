Feature: phonebook group edit

    Scenario: group
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on phonebook
        And check edit button is present
        And check edit icon mouse hover text - group
        And click on edit button
        And check elements are present in Edit Group
        And Enter the details into edit group
        And click on update button
        And check if group name is updated or not
        And check if description is updated or not

        And Close driver window