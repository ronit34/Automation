Feature: TUC_child_my_account_edit_fname_and_verify_in_tuc

  Scenario: TUC_child_my_account_edit_fname_and_verify_in_tuc
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "sales" and password "sales"
        And Click on Sign in Button
        And Click on Profile
        And Click on My Account
        And Edit First Name
        And Click on Save Changes
        And Click Ok on Pop-Up
        And Click on Profile
        And Click on Log Out
        Then Enter Right username "ICICIAdmin" and password "ali"
        And Click on Sign in Button
        And Click on User Management
        And Click On User
        And Verify First Name

        And Close Windows Driver