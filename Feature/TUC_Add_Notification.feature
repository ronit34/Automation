Feature: TUC Add Notification

  Scenario: Add Notification in TUC
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "ICICIAdmin" and password "ali"
#     And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And check Notification is present
    Then click on Notification

    And click on Add Notification

    And select dropdown tuc "Specific TUC"
    And insert data into Tuc Notification fields
    And click on Add Button

    And check Notification is created or not

    And Close driver window