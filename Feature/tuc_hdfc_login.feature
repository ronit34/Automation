Feature: TUC HDFC User Login feature

    Scenario: TUC_HDFC_UserLogin
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "HDFCAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Check todays date is present

        And Close driver window