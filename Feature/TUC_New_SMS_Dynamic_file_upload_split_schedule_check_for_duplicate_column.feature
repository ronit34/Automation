Feature: Dynamic SMS file upload split schedule to check duplicate column

    Scenario: Dynamic SMS file upload split schedule to check duplicate column
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on new SMS
        And Click on Dynamic SMS
        And Choose file for dynamic
        And Select Campaign Name and Sender ID
        And Select Columns
        And Insert Template in Dynamic
        And Click on Schedule SMS
        And Click on Split into multiple Campaigns
        And Split SMS and count
        And Click on send In dynamic sms
        And Click on yes button of pop-up

        And Verify duplicate number
        And Click on proceed
        And Close driver window
