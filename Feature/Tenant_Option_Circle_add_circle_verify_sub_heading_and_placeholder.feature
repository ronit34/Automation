Feature: Tenant_Option_Circle_add_circle_verify_sub_heading_and_placeholder
  Scenario: Tenant_Option_Circle_add_circle_verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button
        Then Click on Option
        And Click on Circle
        And Click on Add Circle
        And Verify Sub-heading and Placeholder_Option Circle

        And Close driver window