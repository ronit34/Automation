Feature: validate dlt text

    Scenario: Login to Onextel localhost and validate DLT tabs
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on the DLT button
        And check if DLT text is present or not
        And check if Entity ID text is present or not
        And check if EntityName text is present or not
        And check if Action text is present or not in dlt entity id
        And click on add entity id button
        And check if Add Entity ID text is present or not
        And check if Entity ID text inside add entity id button is present or not
        And check if Entity Name text is present or not

        And Close driver window
