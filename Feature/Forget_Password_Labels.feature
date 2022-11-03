Feature: Forget Password Labels

    Scenario: Forget Password
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsaa"
        And Click on Sign in Button
        And Check text of error message
        And Check for Forget Password text
        And Click on Forget Password
        And Check text of Forget Password
        And Check description text
        And Check text of Reset Password button
        And Close driver window

