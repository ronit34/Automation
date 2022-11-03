Feature: TUC_Growtel_check_otp_box_with_special_char

  Scenario: TUC_Growtel_check_otp_box_with_special_char
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "growronit" and password "growronit"
        And Click on Sign in Button
        And Enter OTP in special character
        And Verify character available or not
        And Close driver window