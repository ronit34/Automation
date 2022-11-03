Feature: Tuc Delete check

    Scenario: :
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And check TUC is present there
        And check delete icon mouse hover text - tuc
        And check TUC is able to delete or not by clicking on delete option
        And check error message is present
        And chekc error label is present
        And click on close button

        And Close driver window