Feature: phonebook final delete

    Scenario: phonebook delete
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check phonebook is present
        Then click on phonebook
        And check delete icon is present in group tab
        And check delete icon mouse hover text - final_delete
        And click on delete icon in group tab
        And check if warning message present in group tab

        And Close driver window