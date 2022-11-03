Feature: TUC_Growtel_check_resend_btn_and_verify_error_labels

  Scenario: TUC_Growtel_check_resend_btn_and_verify_error_labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "growronit" and password "growronit"
        And Click on Sign in Button
        And verify resend button error label
        And Close driver window