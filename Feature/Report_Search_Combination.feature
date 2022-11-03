Feature: Report Search Combination

    Scenario: Search Combination
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on report
        And click on report_search button
        And Enter Sender_id
        And Click on search_button
        And Check appearing message
        And Enter mobile and sender_id
        And Click on search_button
#        And Enter UUID
#        And Click on search_button
        And Click on reset_button
        And Change Source type
        And Click on search_button
        And Click on reset_butt
        And Select different tuc
        And select from date "22042022"
        And Set limit to 5
        And Enter mobile and sender_id
        And Click on search_button

        And Close driver window
