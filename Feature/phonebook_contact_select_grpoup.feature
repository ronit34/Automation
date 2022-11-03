Feature: phonebook contact d\select group

    Scenario: select group
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on phonebook
        And click on contact
        And click on select group and select contact
        And check contact is showing

        And Close driver window