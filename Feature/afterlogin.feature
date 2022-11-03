Feature: After Login

    Scenario: Login Successful
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then Check Dashboard should present
        Then Check Admin should present
        Then click on dropdown of super admin onextel
        And check present My Account
        And check present alert
        And check present change password
        And check present log out
#        Then check left Margin Super TUC present
        Then check left Margin Dashboard present
        Then check left Margin User Management present
        And check check credit allocation is present
        And check master balance is present
        And check master license is present
        And Close driver window




