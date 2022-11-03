Feature: SA Spam add category

    Scenario: Spam add category
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Click on Sign in Button

        And Click on Spam
        And check delete icon mouse hover text - SA_category
        And Click on Delete Icon
        And click   Delete

        And Close driver window
