Feature: TUC UserMgmt Download User

    Scenario: TUC UserMgmt Downlaod User
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Click on User_Management
        And Click on User Button
        And click on download file
        And select file type to download
        And Click on download of pop up window
        And close browser
