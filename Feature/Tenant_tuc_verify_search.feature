Feature: Tenant user search filters check

  Scenario Outline: TA user search
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "Onexadmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And Click on User_Management
    And type username "<input1>" and verify search results in tuc tab
    Examples:
      | input1 |
      | ici    |
      | hdfc   |
      | hic    |
    And check for invalid input in tuc "("



