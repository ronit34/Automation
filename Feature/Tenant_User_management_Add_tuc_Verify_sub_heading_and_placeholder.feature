Feature: Tenant_User_management_Add_tuc_Verify_sub_heading_and_placeholder
  Scenario: Tenant_User_management_Add_tuc_Verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button
        Then click on User_Management
        And Click on Add_TUC
        And Verify Sub-heading and Placeholder

        And Close driver window