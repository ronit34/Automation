Feature: Tenant URL Delete

    Scenario: URL Delete
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on URL of tenant
        And click on delete icon of URl
        And click on Delete button to delete url

        And Close driver window