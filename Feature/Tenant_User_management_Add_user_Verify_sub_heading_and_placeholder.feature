Feature: Tenant_User_management_Add_user_Verify_sub_heading_and_placeholder
  Scenario: Tenant_User_management_Add_user_Verify_sub_heading_and_placeholder
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button
        Then click on User_Management
        And Click on User
        And Click on Add_User
        And Verify Sub-heading and Placeholder_add_user

        And Close driver window