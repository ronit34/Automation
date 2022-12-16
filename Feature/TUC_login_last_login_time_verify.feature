Feature: TUC_login_last_login_time_verify

    Scenario: TUC_login_last_login_time_verify
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected

        And Click on Sign in Button
        And Stored time now
        And Click on profile Login History
        And Verify last login time
        And Close window driver
