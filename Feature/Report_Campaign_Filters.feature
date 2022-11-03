Feature: Report campaign filters

  Scenario: Campaign report apply filters
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    And click on report in left menu

    And click on campaign tab in report
    And click on Search Button in campaign
#    And select Tuc with and check no report data
#    And select TUC from dropdown
#    And Enter TUC Name to search

    And select from date "12042022"
#    And select to date "14042022"
    And click on Search Button in campaign

    And Close driver window


