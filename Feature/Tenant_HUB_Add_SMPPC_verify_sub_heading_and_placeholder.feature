Feature: Tenant_HUB_Add_SMPPC_verify_sub_heading_and_placeholder
  Scenario: Tenant_HUB_Add_SMPPC_verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button
        Then Click on HUB
        And Click on SMPPC
        And Click on Add SMPPC
        And Verify Sub-heading and Placeholder_SMPPC

        And Close driver window