Feature: TUC_login_last_login

    Scenario: TUC_login_last_login
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Click on new sms
        And Click on quick english sms
        And Verify insert template pop-ups and button
        And Verify insert URL and button
        And Click on new sms
        And Click on quick unicode sms
        And Verify insert template pop-ups and button
        And Verify insert URL and button
        And Click on new sms
        And Click on dynamic sms
        And Verify insert template pop-ups and button
        And Verify insert URL and button
        And Click on new sms
        And Click on campaign sms
        And Verify insert template pop-ups and button
        And Verify insert URL and button

        And Click on campaign
        And Verify Campaign description pop-up
        And Verify Action edit pop-up and delete pop-up
        And Click on Add Campaigns
        And Verify Add campaign

        And Click on User Management
        And Click on delete button and verify pop-up in TUC
        And Click on User in User management
        And Click on delete button and verify pop-up in User

        And Click on Credits
        And Click on Update Credit in TUC
        And Verify update credit pop-up and update and cancel button

        And Click on DLT
        And Entity ID Action tab click on edit button and verify pop-up
        And Entity ID Action tab click on delete button and verify pop-up
        And Click on Add Entity ID
        And Verify Entity id pop-up and add and cancel button
        And Click on Sender IDs
        And Sender IDs Action tab click on edit button and verify pop-up
        And Sender IDs Action tab click on delete button and verify pop-up
        And Click on Add Sender ID
        And Verify Sender id pop-up and add and cancel button
        And Click on Template
        And Click on add template
        And Verify template pop-up and add and cancel button
        And Click on delete selected
        And Verify delete selected pop-up and ok and cancel button
        And Click on delete all
        And Verify delete all pop-up and cancel button
        And Template Action tab click on delete button and verify pop-up
        And Click on URL in DLT
        And Click on Add Short URL in DLT
        And Verify add short url pop-up and add and cancel button

        And Click on SMPP
        And Click on delete button of action and verify pop-up and close button

        And Click on API
        And Click on Generate API
        And Verify generate API pop-up
        And Verify API Edit pop-up
        And Verify API Delete pop-up

        And Click on Phonebook
        And Phonebook group Action tab click on edit button and verify pop-up
        And Phonebook group Action tab click on delete button and verify pop-up
        And Click on Add group
        And Verify add group in phonebook
        And Click on Contacts
        And Phonebook contacts Action tab click on edit button and verify pop-up
        And Phonebook contacts Action tab click on delete button and verify pop-up
        And Click on add contacts
        And Verify add contacts pop-up
        And Verify delete selected in contacts
        And Verify delete all in contacts

        And Click on Config
        And Click on Blacklist Category
        And Config blacklist category Action tab click on edit button and verify pop-up
        And Config blacklist category Action tab click on delete button and verify pop-up
        And Click on Add Blacklist in blacklist category
        And Verify add blacklist pop-up in blacklist category
        And Click on blacklist Number
        And verify delete selected in add blacklist number
        And verify delete all in add blacklist number
        And Config blacklist Number Action tab click on edit button and verify pop-up
        And Config blacklist Number Action tab click on delete button and verify pop-up
        And Config blacklist Number Description tab click on description and verify pop-up
        And Click on Whitelist category
        And Config Whitelist category Action tab click on edit button and verify pop-up
        And Config Whitelist category Action tab click on delete button and verify pop-up
        And Click on Add Whitelist in Whitelist category
        And Verify Add Whitelist pop-up in Whitelist category
        And Click on Whitelist Number
        And verify delete selected in add Whitelist number
        And verify delete all in add Whitelist number
        And Config Whitelist Number Action tab click on edit button and verify pop-up
        And Config Whitelist Number Action tab click on delete button and verify pop-up
        And Config Whitelist Number Description tab click on description and verify pop-up

        And Click on Notification
        And Verify Content pop-up in Notification
        And Click on Add Notification
        And Verify Add Notification pop-up
        And Notification Action tab click on edit button and verify pop-up
        And Notification Action tab click on delete button and verify pop-up

        And Close Window Driver