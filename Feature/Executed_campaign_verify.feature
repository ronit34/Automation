Feature: executed campaign check

    Scenario: verify e
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

       And click on new sms
       And click on quick sms
       And click on View Schedule
       And check the campaign is executed or not

       And Close driver window