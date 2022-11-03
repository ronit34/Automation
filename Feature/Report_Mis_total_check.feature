Feature: Report Mis total check

  Scenario: total check in Mis
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    And click on report in left menu
    And click on search in MIS tab
    ##############################
    And click on the total mis counts
    And click on search in MIS
    And check web count and submitted count
    ##############################
    And click the Download Button in MIS Report
    And select Download file type
    And Click on okay in the pop up
    And click on download data
    And click on download icon

    And Close driver window


