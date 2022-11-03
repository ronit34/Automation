Feature: Report Campaign Summary Search using Campaign Name and TUCs

  Scenario: Report Search using Campaign Name and TUC Name
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And click on report in left menu
    And click on campaign summary tab in report
    And Enter Specific TUC to see data
    And Select Campaign Name from campaign dropdown
    And click on Search Button in campaign
    And Verify that Campaign Name is same as applied filter
    And Verify that TUC Name is same as applied filter
    And Verify that TUC ID is same as applied filter
    And click the Download Button in MIS Report
    And select Download file type in campaign
    And Click on okay in pop up
    And click on download data
    And click on download icon

    And Close driver window