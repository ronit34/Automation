Feature: TUC_Growtel_uncheck_2fa_and_verify_remove_or_not

  Scenario: TUC_Growtel_uncheck_2fa_and_verify_remove_or_not
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "growtelronit" and password "growtelronit"
        And Click on Sign in Button
        Then click on User_Management
        And Click on Edit tuc
        And uncheck 2fa and update

        And Click User Profile and logout
        And Enter Right username "growronit" and password "growronit"
        And Click on Sign in Button
        And Verify login or not
        And Close driver window