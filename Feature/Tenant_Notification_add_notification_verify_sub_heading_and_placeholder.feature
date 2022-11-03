Feature: Tenant_Notification_add_notification_verify_sub_heading_and_placeholder
  Scenario: Tenant_Notification_add_notification_verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button
        Then Click on Notification
        And Click on Add Notification
        And Verify Sub-heading and Placeholder_Notification

        And Close driver window