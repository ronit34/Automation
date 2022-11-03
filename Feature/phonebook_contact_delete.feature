Feature: phonebook delete contact

    Scenario: delete contact
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check phonebook is present
        Then click on phonebook
        And click on contacts tab
        And select phonebook group
        And search
        And check delete icon is present or not
        And check delete icon mouse hover text - contact
        And click on delete icon
        And check popup appear or not
        And click on delete button inside contact tab

        And Close driver window