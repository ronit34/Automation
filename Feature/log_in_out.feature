Feature: log in_out

    Scenario: in_out
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then check log_in_out for all pages