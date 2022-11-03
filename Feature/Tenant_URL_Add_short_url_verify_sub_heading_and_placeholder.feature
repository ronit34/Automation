Feature: Tenant_HUB_Add_url_verify_sub_heading_and_placeholder
  Scenario: Tenant_HUB_Add_url_verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button
        Then Click on URL in tenant
        And Click on Add Short URL
        And Verify Sub-heading and Placeholder_Routing

        And Close driver window