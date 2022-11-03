Feature: New SMS Unicode Input short recipients

    Scenario: Unicode short recipients SMS
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on new sms
        And click on Unicode sms
        And select sender id
        And Insert hindi long var Template
        And select the Allow Multi Part SMS checkbox
        And click on send now button "7"

        And Close driver window