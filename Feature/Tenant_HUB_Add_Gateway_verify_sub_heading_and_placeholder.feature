Feature: Tenant_HUB_Add_Gateway_verify_sub_heading_and_placeholder
  Scenario: Tenant_HUB_Add_Gateway_verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button
        Then Click on HUB
        And Click on Add Gateway
        And Verify Sub-heading and Placeholder_Gateway

        And Close driver window