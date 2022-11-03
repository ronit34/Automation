Feature: Login feature

    Scenario: Check logo of login page
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then verify that the inner text present on page
        And verify picture is present
        And verify the message is present
        And verify the user textbox is present
        And verify the password textbox is present
        And verify the eye button is present
        And verify the user placeholder is present
        And verify the Password placeholder is present
        And Check Terms And Conditions Check Box is preselected
        And verify sign in button is present




