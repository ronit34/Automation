Feature: TUC_Growtel_edit_of_tuc_invalid_email_and_number

  Scenario: TUC_Growtel_edit_of_tuc_invalid_email_and_number
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "growtelronit" and password "growtelronit"
        And Click on Sign in Button
        Then click on User_Management
        And Click on User
        And Click on Edit user
        And Enter invalid email and number and update

        And Click User Profile and logout
        And Enter Right username "growronit" and password "growronit"
        And Click on Sign in Button
        And Check invalid email and number are present or not
        And Close driver window