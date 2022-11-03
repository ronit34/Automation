Feature: sa Spam Labels

    Scenario: Spam Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "onexsa" and password "onexsa"
        And Click on Sign in Button

        And Click on Spam
        And Click on Keywords tab
        And Select Category in keyword tab
        And Click   Search
        And check edit icon mouse hover text - keyword
        And click on edit icon in keyword
        And edit spam keyword
        And Click Add
        And check keyword updated or not

        And Close driver window
