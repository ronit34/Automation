Feature: TUC_Phonebook_create_group_upload_file_again_upload_same_file_check_close_and_cancel_btns

    Scenario: TUC_Phonebook_create_group_upload_file_again_upload_same_file_check_close_and_cancel_btns
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on Phonebook
        And Click on add group in phonebook
        And Insert group details
        And Click on Add button
        And Click on Contacts
        And Click on Add Contacts
        And Choose Upload Bulk Contact
        And Choose for upload a number file
        And Click on close button in phonebook contact
        And Click on Add Contacts
        And Choose Upload Bulk Contact
        And Choose for upload again same number file
        And Click on cancel button in phonebook contact
        And Close driver window

