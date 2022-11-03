Feature: Unicode SMS long Url

    Scenario: unicode long url recepients
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms button
        And click on Unicode sms
        And select sender id
        And select test group

        And Insert hindi long var Template
        And Insert URL for unicode long
        And select the Allow Multi Part SMS checkbox
        And click on allow unicode
        And click on SEND butn
#        And we are trying to send sms
        And check change in credits after sms is sent "161"

        And Close driver window
