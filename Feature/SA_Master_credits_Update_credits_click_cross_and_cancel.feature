Feature: Credits click cross and cancel

  Scenario: Credits click cross and cancel
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "onexsa" and password "onexsa"
        And Click on Sign in Button
        And Click on Master Credits
        And Click on Update credits and click cross and cancel button
        And Close Windows Driver