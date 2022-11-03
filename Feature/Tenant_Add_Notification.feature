Feature: Tenant Add Notification

  Scenario: Add Notification in Tenant
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "Onexadmin" and password "ali"
#     And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And check Notification is present
    Then click on Notification

    And click on Add Notification
    And select dropdown tuc "TUC with children"
    And insert data into Notification fields
    And click on Add Button
    And check Notification is created or not

    And Close driver window
