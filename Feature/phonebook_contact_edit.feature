Feature: phonebook contact edit

    Scenario: contact edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check phonebook is present
        Then click on phonebook
        And  check Contacts text is present
        And click on contacts tab
        And select phonebook group
        And search
        And check edit button  in contacts tab is present
        And check edit icon mouse hover text - phonebook
        And click on edit button on contacts tab
        And check elements are present in Edit Group of contacts tab
        And Enter the details into edit group of contacts tab
        And click on update button of contacts tab
        And check name is updated or not

        And Close driver window