Feature: TUC_DLT_template_search_type_template_id_enter_template_id_select_template_and_delete_selected

    Scenario: TUC_DLT_template_search_type_template_id_enter_template_id_select_template_and_delete_selected
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on DLT
        And Click on Template
        And Select search type template id
        And Enter template id in template-
        And Click on Search in template

        And Select a template and delete selected

        And Close window driver