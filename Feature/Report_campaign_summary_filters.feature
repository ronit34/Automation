Feature: Report campaign summary filters

  Scenario: campaign summary report filters apply
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    And click on report in left menu
    And click on campaign summary tab in report
    And click on Search Button in campaign
  ###################  APPLY FILTERS ##################
    And verify submitted count
#    And select TUC from dropdown
    And select from date "12042022"
    And select campaign name
    And set limit and check pagination in campaign summary
    And verify submitted count
    ################### DOWNLOAD FILE ###################
    And click the Download Button in MIS Report
    And select Download file type in campaign
    And Click on okay in pop up
    And click on download data
    And click on download icon

    And Close driver window