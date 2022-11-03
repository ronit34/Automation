Feature: Forget Password Functionality

    Scenario: Forget Password Function
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsaa"
        And Click on Sign in Button
        And Check text of error message
        And Click on Forget Password
        And Check username field is present or not
        And Enter wrong username
        And Click on Reset password button
        And Check for error message appeared
#        And Enter correct username of which password has be reste
#        And Click on Reset password button
#        And Check for appeared message
        And Close driver window

