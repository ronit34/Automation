Feature:  Same Name TUC Validation

    Scenario: : TUC Validation
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And Click on User_Management
        And Click on Add Tenant Button

        And insert elements in add tuc
        And click on create button to save it
        And Check for appeared Error Label

        And Close driver window
