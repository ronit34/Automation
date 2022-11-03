Feature: Template URL Edit

    Scenario: Template URL
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Click on URL of tenant
        And click on edit of url
        And enter new url
        And click on update to update url
        And check edited url

        And Close driver window