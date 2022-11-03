Feature: onexsa login

    Scenario: iterate
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then check iteratively login
