Feature: TUC_Config_blacklist_unicode_csv

    Scenario:  TUC_Config_blacklist_unicode_csv
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        Then click on Config
        And Click on Add Blacklist Category
        And Insert category name and category description
        And Click on add button in blacklist category

        Then Click on blacklist Number
        And Click on Upload Blacklist_number
        And Choose csv unicode file for blacklist
        And Select Category in blacklist
        And Add records to category
        And Click on Ok button in blacklist
        And Close driver window

