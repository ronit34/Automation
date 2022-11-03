Feature: SA_Master_Credits_update_credits_Verify_sub_heading_and_placeholder

    Scenario: SA_Master_Credits_update_credits_Verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Click on Spam
        And Click on Add Category
        And Verify Sub-heading and Placeholder Create Spam Category
        And Close driver window
