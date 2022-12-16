Feature: TUC_DLT_template_search_type_template_id_enter_template_name_verify_error_label

    Scenario: TUC_DLT_template_search_type_template_id_enter_template_name_verify_error_label
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on DLT
        And Click on Template
        And Select search type template id
        And Enter template name in template
        And Click on Search in template

        And Verify error label in template
        And Click on reset template
        And Verify data present or not
        And Close window driver