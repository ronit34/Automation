Feature: TUC_login_last_login

    Scenario: TUC_login_last_login
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected

        And Click on Sign in Button
        And Stored last login time data
        And Click on profile Login History
        And Verify last login time history
        And Close window driver
