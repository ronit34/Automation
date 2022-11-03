Feature: tenant user search download

    Scenario: Tenant_Customer_User search download
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Click on User_Management
        And Click on User Button
        And enter data in search bar in user "icici"
        And click on search button in tuc
#        And verify search in table
        And click on download file
        And select file type to download
        And close browser
