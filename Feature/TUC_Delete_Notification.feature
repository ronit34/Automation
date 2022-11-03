Feature: TUC Delete Notification

  Scenario: Delete Notification in TUC
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "ICICIAdmin" and password "ali"
#     And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And check Notification is present
    Then click on Notification

    And click on Delete
    And click on Delete Button to delete

    And Close driver window