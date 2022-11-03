Feature: TUC_DLT_Bulk_upload_files_of_missing_senderid_tempname_temptype_tempid_in_bulk_upload_and_check

    Scenario: TUC_DLT_Bulk_upload_files_of_missing_senderid_tempname_temptype_tempid_in_bulk_upload_and_check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        Then click on DLT
        Then Click on Bulk Upload
        Then Select Entity Id
        Then Select jio operator
        And choose file for jio_sender_id_missing_file
        Then Click on save templates
        And check sender_id Failed missing popup
        Then click on OK button in bulk_upload

        Then Click on Bulk Upload
        Then Select Entity Id
        Then Select jio operator
        And choose file for template_id_missing_file
        Then Click on save templates
        And check error file content invalid

        Then Click on Bulk Upload
        Then Select Entity Id
        Then Select jio operator
        And choose file for template_name_missing_file
        Then Click on save templates
        And check template_name already exist
        Then click on OK button in bulk_upload

        Then Click on Bulk Upload
        Then Select Entity Id
        Then Select jio operator
        And choose file for template_type_missing_file
        Then Click on save templates
        And check template_name already exist
        Then click on OK button in bulk_upload

        Then Click on Bulk Upload
        Then Select Entity Id
        Then Select jio operator
        And choose file for jio
        Then Click on save templates
        And check template_name already exist
        Then click on OK button in bulk_upload

        And close browser