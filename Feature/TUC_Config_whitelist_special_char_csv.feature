Feature: TUC_Config_whitelist_special_char_csv

    Scenario:  TUC_Config_whitelist_special_char_csv
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        Then click on Config
        And Click on Whitelist Category
        And Click on Add Whitelist Category
        And Insert category name and category description in whitelist
        And Click on add button in whitelist category

        Then Click on whitelist Number
        And Click on Upload Whitelist_number
        And Choose csv file for whitelist
        And Select Category in whitelist
        And Add records to category
        And Click on Ok button in whitelist
        And Close driver window

