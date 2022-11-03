Feature: TUC_menu_label_check

    Scenario: Tuc Menu
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check label of Dashboard
        And check label Campaign
        And check label of user management
        And check label Credits
        And check label of Report
        And check label of TUC Telco Reports
        And check label of DLT
        And check label of SMPP
        And check label of API
#        And check label Approvals
        And check label of Phonebook
        And check label of Config
        And check label of TUC Notification

        And Close driver window