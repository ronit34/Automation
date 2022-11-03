Feature: Campaign SMS Short Url normal

    Scenario: campaign short url normal
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms button
        And click on campaign sms
        And select test group in campaign
        And select a sender id
        And Insert Template
        And Click on Send Button of campaign sms
        And Close driver window

