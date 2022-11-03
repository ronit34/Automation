Feature: DLT URL

    Scenario: DLT URL and labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        And Click on URL
        And Click on Add Short URL
        And Check labels
        And Insert data into URL fields
        And click on add button to add URL
        And Check URL is created or not

        And Close driver window