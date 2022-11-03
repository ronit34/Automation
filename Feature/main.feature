Feature: Main

    Scenario: Login Successful
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Check if the message invalid login then close the browser
        Then Check Dashboard should present
        Then Check Admin should present
        Then click on dropdown of super admin onextel
        And check present My Account
        And check present alert
        And check present change Number or Mail
        And check present change password
        And check present credit history
        And check present log out
        Then check left Margin Super TUC present
        Then check left Margin Dashboard present
        Then check left Margin User Management present
        Then Close Browser


    Scenario: Check logo of login page
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then verify that the logo present on page
        And verify picture is present
        And verify the message is present
        And verify the user textbox is present
        And verify the password textbox is present
        And verify the user placeholder is present
        And verify the Password placeholder is present
        And verify sign in button is present
        And close browser



