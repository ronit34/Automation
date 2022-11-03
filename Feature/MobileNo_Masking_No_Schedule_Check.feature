Feature: Mobile Number Masking No Schedule Check

    Scenario: Masking No Schedule Check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms
        And click on quick sms
        And insert data into quick sms
        And Schedule sms
        And click on send button
        And click on send now button of dynamic sms
        And click on View Schedule button
        And click on report
        And click on search in MIS tab
        And click on the total mis counts
        And click on mis web search
        And click on mis web detail button
        And check for mobile no masking

        And Close driver window
