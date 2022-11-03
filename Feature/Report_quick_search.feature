Feature: Report Quick SMS Search

    Scenario: Quick Search
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And sent sms through qucik
        And click on report_search option
        And Then Check sent sms is in report or not
        And close report quick search