Feature: SA_Notification_Add_Notification_Verify_sub_heading_and_placeholder

    Scenario: SA_Notification_Add_Notification_Verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Click on Notification
        And Click on Add Notification
        And Verify Sub-heading and Placeholder Add Notification
        And Close driver window
