Feature: SA Spam add category

    Scenario: Spam add category
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Click on Sign in Button

        And Click on Spam

         And check edit icon mouse hover text - Spam_Category

        And click on edit icon against category name
        And edit category name
        And click Update Btn
        And check updated category name

        And Close driver window


