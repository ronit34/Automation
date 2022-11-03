Feature: TUC_Growtel_enter_invalid_otp_and_verify_error_labels

  Scenario: TUC_Growtel_enter_invalid_otp_and_verify_error_labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "growronit" and password "growronit"
        And Click on Sign in Button
        And Enter invalid otp
        And Verify error label
        And Close driver window