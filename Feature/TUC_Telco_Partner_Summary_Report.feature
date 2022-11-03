Feature: TUC Telco partner summary

  Scenario: Partner_Summary
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
#    Then Check if the message invalid login then close the browser
    And click on telco reports
    And click on Search of partner summary
    And click on download of partner summary
    And Close driver window