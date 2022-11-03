Feature: DLT URL LABELS

    Scenario: DLT ids and labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check DLT is present
        Then click on DLT
        Then click on url
        And check text of url
        And check text of url status
        And check text of url action
        And click on Add short url
        And check text of Add Short URL
        And check text of url label
        And check text of cancel url
        And check text of add url
        And check text inside place holder

        And Close driver window

