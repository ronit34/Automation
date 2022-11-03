Feature: Report Search Download

    Scenario: Search Download
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
#        And sent sms through qucik
        And click on report
        And click on campaign_search option
        And Then Check sent sms is in report or not
        And click on Download button
        And go to download data section and download the file

        And Close driver window