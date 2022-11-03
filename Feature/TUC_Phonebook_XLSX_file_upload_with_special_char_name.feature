Feature: TUC_Phonebook_XLSX_file_upload_with_special_char_name

    Scenario: TUC_Phonebook_XLSX_file_upload_with_special_char_name
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Click on Sign in Button

        Then click on phonebook
        And Click on Add Group
        And Insert group name and description
        And Click on Add in add group of phonebook
        And click on contact
        And click on the Add contacts tab in phonebook
        And select the Upload Bulk Contact option inside add contacts tab in phonebook
        And choose the file to upload xlsx file
        And select the group to which you want to add contact
        And finally click on add button

        And Close driver window