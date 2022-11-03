Feature: ICICI Masking Edit

    Scenario: Masking Edit to No
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on User_Management
        And Click on edit button of ICICI
        And Select mask number as NO
        And click on update button to update mask number

        And Close driver window
