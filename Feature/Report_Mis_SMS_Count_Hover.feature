Feature: Report MIS SMS Count Hover Check

  Scenario: SMS Count Hover Check
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    And click on report in left menu
    And click on search in MIS tab

    And click on the total mis counts
    And click on mis web search
    And Hover on first number under SMS Count

    And Close driver window
