Feature: Tenant_Option_Vendor_add_vendor_verify_sub_heading_and_placeholder
  Scenario: Tenant_Option_Vendor_add_vendor_verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button
        Then Click on Option
        And Click on Vendor
        And Click on Add Vendor
        And Verify Sub-heading and Placeholder_Option Vendor

        And Close driver window