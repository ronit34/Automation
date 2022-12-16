Feature: TUC_download_template_and_verify_downloaded_file

    Scenario: TUC_download_template_and_verify_downloaded_file
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on DLT
        And Click on Template
#        And Click on Download
        And Click on Download Pop-up
        And Download Template and verify file is empty or not
        And Close window driver