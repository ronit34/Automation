Feature: Delete_the_particular_TA_created

    Scenario: Delete_the_particular_TA_created
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then Click on User_Management
        And Delete the perticular TA
        And Click on delete in User_Management
        And Close driver window