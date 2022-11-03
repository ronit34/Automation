Feature: quick promo

    Scenario: quick recipients promo
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And click on new sms
        And click on quick sms
        And insert data for promo quick
        And select Promo template
        And check Scrub Dnd checkbox is selected
        And click on SEND butn
        And click on send now
        And close browser



