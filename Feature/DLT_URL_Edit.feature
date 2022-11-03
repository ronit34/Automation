Feature: DLT URL Edit

    Scenario: DLT URL Edit labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        And Click on URL
        And check edit icon mouse hover text - dlt url
        And Click on Edit icon of URL
        And Check Edit Labels
        And Insert data into Update URL fields
        And click on Update button to add URL
        And Check URL is edited or not

        And Close driver window