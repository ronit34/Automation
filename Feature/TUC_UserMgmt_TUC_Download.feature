Feature: TUC UserMgmt Download TUC

    Scenario: TUC UserMgmt Downlaod TUC
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Click on User_Management
        And click on download file
        And select file type to download
        And Click on download of pop up window
        And close browser
