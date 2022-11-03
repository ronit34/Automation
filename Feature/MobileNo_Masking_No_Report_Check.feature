Feature: Mobile Masking No Check

    Scenario: Masking check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Check if the message invalid login then close the browser
        And click on new sms
        And click on quick sms
        And insert data into quick sms
        And Click on Send Button of quick sms
        And click on cancel of pop up
        And click on report
        And click on search in MIS tab
        And click on the total mis counts
        And click on mis web search
        And click on mis web detail button
        And Check mobile Number is not masked
        And Copy UUID and enter it in Report Search
        And Click on search_button
        And check mobile number is not masked in search

        And Close driver window