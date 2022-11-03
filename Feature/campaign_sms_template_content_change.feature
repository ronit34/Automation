Feature: Campaigm message

    Scenario: new campaign message
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And click on new sms
        And click on campaign sms
        And sent sms through campaign
        And click on reports
        And click on Campaigns
        And click on download

        And Close driver window


