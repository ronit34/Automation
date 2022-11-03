Feature: TUC SMS Balance Deduction

    Scenario: Bal Deduction
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And first check available credits
#        And click on new sms
#        And create multiple quick sms
#        And check cost is deducted as per credit alloted

        And Close driver window