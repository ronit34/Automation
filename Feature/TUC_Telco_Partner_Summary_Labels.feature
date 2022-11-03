Feature: TUC Telco Partner Summary Reports

  Scenario: Lables
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
#    Then Check if the message invalid login then close the browser
    And click on telco reports
    And check text of partner summary
    And check text of From of partner summary
    And check text of To of partner summary
    And check text of Search Button of partner
    And click on Search of partner summary

    And check text of TUC NAME of partner summary
#    And check text of Submitted of partner summary
    And check text of Credits of partner summary
    And check text of Delivered of partner summary
    And check text of Failed of partner summary
    And check text of Awaited of partner summary
#    And check text of Totals of partner summary in tuc
    And Close driver window
