Feature: New SMS Campaign Insert Template

    Scenario: Insert Template
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms
        And click on campaign sms
        And choose numbers file
        And select a sender id

        And select Promo template
        And check Scrub Dnd checkbox is selected
        And click on SEND butn
        And click on send now
        And close browser
