Feature: TUC_template_search_type_template_name_enter_template_name_set_limit_check_pagination_working_or_not

    Scenario: TUC_template_search_type_template_name_enter_template_name_set_limit_check_pagination_working_or_not
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on DLT
        And Click on Template
        And Select search type template name
        And Enter template name
        And Click on Search in template
        And Click on set limit and check pagination working or not
        And Close window driver

