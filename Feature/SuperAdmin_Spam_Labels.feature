Feature: Super Admin Spam Labels

    Scenario: Spam Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Click on Sign in Button

        And Click on Spam
        And Check for Spam header

        And Check text of Spam Category
        And Check text of Keywords
        And check text of Category Assign

        And Click on Spam Category
        And Check for Category Name tab
        And Check for Action tab
        And Check text of Add Category Button

        And Click on add Category Button
        And Check for Add Spam Category
        And Check for Category Text
        And Check for Cancel Buttn
        And Check for Add Button
        And Click on Cross Button

        And Click on Keywords tab
        And Check for Select Category text
        And Check for search text
        And Check for Add Keywords text
        And Click on Add Keywords
        And Check for Add Spam Category text
        And Check for Select Category text
        And Check for Spam Keywords text
        And Check for Add Keywords text button
        And Check for Cancel Buttn
        And Check for Add Button
        And Click on Cross Button

        And Click on Category Assign tab
        And Check for Select Category text
        And Check for search text
        And Check for Add TUCs text
        And Click on Add TUCs
        And Check for Add TUCs
        And Check for select category
        And Check for TUCs
        And Check for Cancel Buttn
        And Check for Add Button
        And Click on Cross Button

        And Close driver window