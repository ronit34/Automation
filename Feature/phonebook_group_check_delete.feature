Feature: phonebook Group check delete

    Scenario: check delete
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check phonebook is present
        Then click on phonebook
        And check delete button is present
        And check delete icon mouse hover text - group
        And click on delete button
        And check the warning message is present
        And click on cancel button

        And Close driver window