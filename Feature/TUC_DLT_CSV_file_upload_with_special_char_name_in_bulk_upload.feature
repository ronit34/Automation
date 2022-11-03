Feature: TUC_DLT_CSV_file_upload_with_special_char_name_in_bulk_upload

    Scenario: TUC_DLT_CSV_file_upload_with_special_char_name_in_bulk_upload
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        Then click on DLT
        Then Click on Bulk Upload
        Then Select Entity Id
        Then Select jio operator
        And choose csv file for jio operator
        Then Click on save templates
        And check message on popup
        Then click on OK button in bulk_upload