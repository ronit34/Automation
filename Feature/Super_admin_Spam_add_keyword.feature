Feature: sa Spam Labels

    Scenario: Spam Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Click on Sign in Button

        And Click on Spam
        And Click on Keywords tab
        And Click on Add Keywords
        And Select Category from Dropdown
        And enter first spam keyword
        And click on add keyword button
        And enter second spam keyword
        And Click Add
        And check if the keyword is added or not

        And Close driver window
