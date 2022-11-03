Feature: Onextel api user login

  Scenario: Login to Onextel api labels localhost
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on the api tab
        And click on Generate api button
        And Select Account from Account Type dropdown
        And click on Submit button of Generate api
        And Verify whether api key for same Account Type is created or not

        And Close driver window