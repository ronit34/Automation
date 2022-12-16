Feature: TUC_template_search_type_template_name_wrong_search_text_search_verify_error_label_click_reset_verify_header

    Scenario: TUC_template_search_type_template_name_wrong_search_text_search_verify_error_label_click_reset_verify_header
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on DLT
        And Click on Template
        And Select search type template name
        And Enter wrong text in search bar
        And Click on Search in template
        And Verify error label of template name
        And Click on reset template
        And Verify headers of template

        And Close window driver