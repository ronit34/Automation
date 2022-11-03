Feature: TUC_Growtel_check_all_btns_of_2fa_page_labels

  Scenario: TUC_Growtel_check_all_btns_of_2fa_page_labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "growronit" and password "growronit"
        And Click on Sign in Button
        And Check all buttons of 2fa page
        And Close driver window