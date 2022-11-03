Feature: TUC credit check

    Scenario: Tuc update credits to child cross check
        Given Launch Chrome Browser
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then click on User_Management
        And Cross verify the Available Credits in Credits tab

      ##########################################################
#       And click on credit allocation
#       And Select Tenant/TUC
#        And click on search button in credits

        And Close driver window
