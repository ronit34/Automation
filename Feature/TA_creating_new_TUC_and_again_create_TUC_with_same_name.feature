Feature: TA_creating_new_TUC_and_again_create_TUC_with_same_name

    Scenario: TA_creating_new_TUC_and_again_create_TUC_with_same_name
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Telspiel" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on User management
        And Click on Add TUC in TA11 for SBI
        And Insert details in add TUC in TA11 for SBI
        And Click on create in add TUC in TA11
        And Verify TUC create or not in TA11
        # Creating again with same name
        And Click on Add TUC in TA11 for SBI
        And Insert details in add TUC in TA11 for SBI
        And Click on create in add TUC in TA11
        And Verify TUC create or not in TA11 which one creating again with same name
        And Close window driver