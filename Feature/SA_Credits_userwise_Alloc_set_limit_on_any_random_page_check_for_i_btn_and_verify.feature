Feature: SA_Credits_userwise_Alloc_set_limit_on_any_random_page_check_for_i_btn_and_verify

    Scenario: SA_Credits_userwise_Alloc_set_limit_on_any_random_page_check_for_i_btn_and_verify
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on credits
        And Click on limit
        And Click on search
        And Click on i button
        And  Verify the text
        And Close driver window