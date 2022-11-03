Feature: check tuc dashboard label

    Scenario: TUC_Dashboard_Label_check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
#        And check whether Not able to load data! text is present
        And check whether No Scheduled Record Found text is present in Scheduled SMS

        And Close driver window