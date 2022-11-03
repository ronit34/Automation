Feature: Onextel hub default gateway tenant login

  Scenario: Login to Onextel   reports labels localhost
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "Onexadmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    And Click on hub
#    And check text of hub
#    And click on Gateway
    And click on  Default Gateway
    And select data from otp
    And select data from Service Implicit
    And select data from Service Explicit
    And select data from Promotional
    And select data from TransPromo
    And select data from Government Exempted
    And select data from Simroute
    And click on Save default gateway
    And click on okay

    And Close driver window