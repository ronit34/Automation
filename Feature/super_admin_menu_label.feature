Feature: Super Admin Menu Label

    Scenario: Menu
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check label of Dashboard
        And check label of user management
        And check label Credits
        And check label of Master Balance
        And check label of Master License

        And Close driver window
