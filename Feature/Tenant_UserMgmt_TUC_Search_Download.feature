Feature: Tenant UserMgmt TUC Search Download

    Scenario: Tenant TUC Search Downlaod
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Click on User_Management

        And enter data in search bar in tuc "icici"
        And click on search button in tuc

        And click on download file
        And select file type to download
        And Click on download of pop up window
        And close browser
