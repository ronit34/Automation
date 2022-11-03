Feature: DLT

  Scenario: DLT search tab
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
#   Then Check if the message invalid login then close the browser
#   And check DLT is present
    Then click on DLT
    And go to search tab
    And click on search in dlt search tab
    And check error label
    And enter 3 characters and check error label
    And input full Template name
#   And click on search and verify data

    And Close driver window