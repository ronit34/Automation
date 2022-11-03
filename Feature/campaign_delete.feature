Feature: delete campaign

    Scenario: : delete steps
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Campaign
        And check delete icon is present inside campaign tab
        And check delete icon mouse hover text - campaign
        And click on delete icon inside campaign tab
        And check popup appear or not in campaign tab
        And click on delete button inside campaign tab

        And Close driver window