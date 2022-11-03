Feature: Super Admin Add Notification

  Scenario: SA Add Notification
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "onexsa" and password "onexsa"
#     And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And check Notification is present
    Then click on Notification

    And Click on Add Notification
    And select dropdown tuc "Tenant/TUC with children"
    And insert data into Notification fields

    And click on Add Button
    And check Notification is created or not

    And Close driver window


