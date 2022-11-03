Feature: validate dlt text

    Scenario: Login to Onextel localhost and validate DLT tabs
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on the DLT button
        And click on Bulk Upload tab
        And check if Entity ID is present or not
        And check if Operator is present or not
        And check if Reset button text is present or not
        And check if Save Templates text is present or not

        And Close driver window



