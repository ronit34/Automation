Feature: Report Mis complete check

  Scenario: Total complete check MIS
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "Onexadmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    And click on report in left menu
    And click on search in MIS tab

    And click on the total counts
    And click on mis web search
    And click on mis web detail button
    And copy UUID and paste in search tab and verify porterid text
    And Close driver window

