Feature: TUC_Growtel_click_resend_btn_after_one_minute_sleep_and_verify_labels

  Scenario: TUC_Growtel_click_resend_btn_after_one_minute_sleep_and_verify_labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "growronit" and password "growronit"
        And Click on Sign in Button
        And Click on resend otp
        And verify after 1 minute
        And Close driver window