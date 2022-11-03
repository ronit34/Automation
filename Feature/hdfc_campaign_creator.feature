Feature: HDFC add input campaign

    Scenario: : Common steps
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "HDFCAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Campaign
        And click on add campaign
        And Enter Name "RCF"
        And Enter Description "It Is Charity Organization"
        Then click on Add Campaign button to create

        And Close driver window
