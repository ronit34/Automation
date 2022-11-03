Feature: tuc search download

    Scenario: Tenant_Customer_User
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And Click on User_Management
        And enter data in search bar "sales"
        And click on search button in tuc
#        And verify search in table
        And click on download file
        And select file type to download
        And close browser
