Feature: Unicode SMS long Url

    Scenario: unicode long group url
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"

        And Click on Sign in Button

        And click on new sms button
        And click on Unicode sms
        And insert data into fields without recipients
        And select test group

        And Insert hindi long var Template
        And select the Allow Multi Part SMS checkbox
#        And click on SEND butn
        And click on send now button "154"

        And Close driver window

