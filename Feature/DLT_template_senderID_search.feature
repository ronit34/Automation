Feature: DLT Template SenderID Search

  Scenario: Template Sender ID Search
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    And check DLT is present
    Then click on DLT
    And click on template tab
    And input wrong senderID in template search
    And input senderID in template search
    And set limit and check pagination in template

    And Close driver window