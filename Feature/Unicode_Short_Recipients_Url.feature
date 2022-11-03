Feature: Unicode SMS Short Url

    Scenario: unicode short url
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms button
        And click on Unicode sms
        And select sender id
#        And Enter Number
        And Insert hindi var Template
        And Insert URL for unicode
        And click on allow unicode
        And click on SEND butn
        And check change in credits after sms is sent "1"

        And Close driver window
