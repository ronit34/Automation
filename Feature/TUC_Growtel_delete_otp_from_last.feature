Feature: TUC_Growtel_delete_otp_from_last

  Scenario: TUC_Growtel_delete_otp_from_last
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "growronit" and password "growronit"
        And Click on Sign in Button
        And Enter OTP
        And Delete OTP from last
        And Close driver window