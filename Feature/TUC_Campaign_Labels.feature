Feature: Onextel campaign user login

  Scenario: Login to Onextel campaign labels localhost
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on the campaign tab

        And check if Campaign header text is present or not
        And check if Campaign Name sub header text is present or not in tuc campaign
        And check if Description sub header text is present or not in tuc campaign
        And check if Action sub header text is present or not in tuc campaign

        And click on add campaign button

        And check if Add Campaign text is present or not
        And check for Campaign Name text inside add campaign button
        And check for Description text inside add campaign button
        And check the text of add button
        And check the text of cancel button

        And Close driver window








