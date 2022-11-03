Feature: UnSuccessful Login

  Scenario Outline: TUC login with multiple parameters
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    And Enter Username "<username>" and password "<password>"
    And Click on Sign in Button for multiple

    Examples:
      | username    | password |
      |             |          |
      | ICICIAdmin  |          |
      |             | ali      |
      | ICICIAAdmin | alii     |
      | ICICIAdmin  | alii     |
      | ICICIAAdmin | ali      |