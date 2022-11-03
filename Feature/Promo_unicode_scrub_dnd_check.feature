Feature: quick promo

    Scenario: quick recipients promo
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And click on new sms
        And click on Unicode sms
        And insert data for promo quick
        And select Promo template for unicode
        And check Scrub Dnd checkbox is selected
#        And select the Allow Unicode checkbox
        And click on send button
        And click on send now button

        And Close driver window





