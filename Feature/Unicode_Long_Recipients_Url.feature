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

        And Insert hindi long var Template
        And Insert URL for unicode long
        And click on allow unicode
        And select the Allow Multi Part SMS checkbox
        And click on SEND butn
        And check change in credits for long url after sms is sent "7"
#        And we are trying to send sms

         And Close driver window