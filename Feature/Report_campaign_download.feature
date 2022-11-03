  Feature: Report campaign download

  Scenario: Campaign report download
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    And click on report in left menu

    And click on campaign tab in report
    And click on Search Button in campaign

    And click the Download Button in MIS Report
    And select Download file type in campaign
    And Click on okay in pop up
    And click on download data
    And click on download icon

    And Close driver window