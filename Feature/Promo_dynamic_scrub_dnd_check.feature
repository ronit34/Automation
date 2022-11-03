Feature: New SMS Dynamic normal

    Scenario: dynamic normal normal
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on Dynamic sms
        And insert data into Dynamic sms for promo
        And check Scrub Dnd checkbox is selected in dynamic
        And click on SEND butn
        And click on send now
        And close browser
