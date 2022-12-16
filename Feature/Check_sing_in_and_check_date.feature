Feature: Check_sing_in_and_check_date

    Scenario: Check_sing_in_and_check_date
        Given launch chrome browser--
        When open Onextel Homepage "http://localhost:8000/index"--
        Then Enter Username "ICICIAdmin" and password "alifvxv"--
        And Check Terms And Conditions Check Box is preselected--
        And Click on Sign in Button--
        And Verify date is present or not--
        And Close window driver--