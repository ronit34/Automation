Feature: SA_Spam_Add_Keywords_Verify_sub_heading_and_placeholder

    Scenario: SA_Spam_Add_Keywords_Verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Click on Spam
        And Click on Keywords
        And Click on Add Keywords
        And Verify Sub-heading and Placeholder Add Span Keywords
        And Close driver window
