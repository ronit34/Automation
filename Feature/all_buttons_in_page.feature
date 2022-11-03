Feature: Context Based page load

    Scenario: Context based page
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then try all in one code
        And Close driver window