Feature: Tenant user search filters check

  Scenario Outline: TA user search
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "Onexadmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And Click on User_Management
    And Click on User Button
    And type username "<input>" and verify search results "user_input"
    Examples:
      | input    |
      | ici      |
      | 12345678 |
      | @        |
      | 1234     |
      | gmail    |
    And check for invalid "z" in search


