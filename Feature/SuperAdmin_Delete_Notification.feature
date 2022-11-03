Feature: SuperAdmin Delete Notification

  Scenario: Delete Notification in SuperAdmin
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "onexsa" and password "onexsa"
#     And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And check Notification is present
    Then click on Notification

    And click on Delete
    And click on Delete Button to delete

    And Close driver window