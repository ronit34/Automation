Feature: Credits add

  Scenario: Credits add
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "onexsa" and password "onexsa"
        And Click on Sign in Button
        And Click on Master Credits
        And Click on Update credits and add few credits point
        And Click on Credit
        And Click on update credits
        And Select Onexmedia and add credits
        And Click on user profile
        And Click on logout
        Then Enter Right username "Onexadmin" and password "ali"
        And Click on Sign in Button
        And Click on Credit
        And Click on update credits
        And Select ICICI and add credits
        And Click on logout
        Then Enter Right username "ICICIAdmin" and password "ali"
        And Click on Sign in Button
        And Verify token add or not
        And Close Window Driver

