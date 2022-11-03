Feature: Onextel api user login

  Scenario: Login to Onextel api labels localhost
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on the api tab
        And check if API text is present or not
        And check if Key text is present or not
        And check if Account Type text is present or not
        And check if Password text is present or not
        And check if Description text is present or not in api
        And check if Status text is present or not in api tab
        And check if Action text is present or not in api tab
        And check text of Generate api button
        And click on Generate api button
        And check if Select Account Type of API text is present or not
        And check if Account Type text in pop up is present or not
        And check if Description text in pop up is present or not
        And check if Send DLR text in pop up is present or not
        And check if Submit text button text is present or not
        And check if cancel button text is present or not

        And Close driver window