Feature: tenant_menu_label_check

    Scenario: Tenant Menu
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check label of Dashboard
        And check label of user management
        And check label Credits
        And check label of Report
        And check label of tenant Telco Reports
        And check label of Hub
        And check label of tenant URL
#        And check label Approvals
#        And check label of tenant Spam
        And check label of Test SMS
        And check label of Monitor
        And check label of Options are present
        And check label of tenant Notification

        And Close driver window
