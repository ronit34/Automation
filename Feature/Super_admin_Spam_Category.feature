Feature: SA Spam add category

    Scenario: Spam add category
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Click on Sign in Button

        And Click on Spam

        And Click on add Category Button
        And fill the category name
        And click on add to add this category
        And check if the category is added or not

        And Close driver window
