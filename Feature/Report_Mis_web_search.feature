Feature: Report Mis search filters

    Scenario: Quick Search
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And click on report in left menu
        And click on search in MIS tab
        And click on the number of sms sent
        And click on search and check if the data is present

        And Close driver window

