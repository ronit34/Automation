Feature: Create a tuc in growtel and verify 2fa

  Scenario: Create a tuc in growtel and verify 2fa
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "growtelronit" and password "growtelronit"
        And Click on Sign in Button
        Then click on User_Management
        And Click on Add TUC for growtel
        And Insert details for growtel tuc
        And  Click on create growtel for tuc
        And Click on User
        And Click on Add User
        And Insert details for growtel in tuc user
        And Click on create growtel for user in tuc

        And Click User Profile and logout
        And Enter Right username "growronit" and password "growronit"
        And Click on Sign in Button
        And Verify 2fa page pop-up is opening or not
        And Close driver window
