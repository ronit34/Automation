Feature: Report Scheduled Campaign Filter Search Using Campaign Name

  Scenario: Report Scheduled Campaign Search using Campaign Name
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And click on report in left menu
    And click on scheduled campaigns tab in report
    And click on Search Button in scheduled campaigns
    And Check for campaign name appearing
    And Select Campaign Name filter from dropdown
    And click on Search Button in scheduled campaigns
    And Verify that Campaign Name is same as applied filter
    And click the Download Button in MIS Report
    And select Download file type in campaign
    And Click on okay in pop up
    And click on download data
    And click on download icon

    And Close driver window