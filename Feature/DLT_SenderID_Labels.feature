Feature: validate dlt text

  Scenario: Login to Onextel localhost and validate DLT tabs
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on the DLT button
        And click on sender ids tab
        And check if Sender ID text is present or not in dlt sender id tab
        And check if Entity ID text is present or not in dlt sender id tab
        And check if Approved By text is present or not in dlt sender id tab
        And check if Approved On text is present or not in dlt sender id tab
        And check if Status text is present or not in dlt sender id tab
        And check if Default text is present or not in dlt sender id tab
        And check if Action text is present or not in dlt sender id tab
        And click on add sender id button in dlt sender id tab
        And check if Add Sender ID text is present or not
        And check if Sender ID text inside add sender id  is present or not
        And check if Select Entity Name text is present or not

        And Close driver window








