Feature: TUC_CSV_File_upload_with_unicode_name_in_Campaign_sms

    Scenario: TUC_CSV_File_upload_with_unicode_name_in_Campaign_sms
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on new SMS
        And Click on Campaign SMS
        And Click on choose csv file with unicode name in campaign
        And select campaign_name and sender_id
        And Insert template
        And Click on send button
        And click on send now button for special char file
        And Close driver window