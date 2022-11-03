Feature: Create a TUC with 2fa and verify 2fa page is opening or not

  Scenario: Create a TUC with 2fa and verify 2fa page is opening or not
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Telspiel" and password "ali"
        And Click on Sign in Button
        Then click on User_Management
        And Click on Add TUC in telspiel with 2fa adn create
        And Click on User
        And Click on Add User and create user
        And Click User Profile and logout
        And Enter Right username "telsronit" and password "telsronit"
        And Click on Sign in Button
        And Verify 2fa page is opening or not
        And Close driver window
