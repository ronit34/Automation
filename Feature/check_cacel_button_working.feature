Feature: check cancel button working

    Scenario: cancel button
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then check in all pages cancel button is working

        And Close driver window