Feature: Tenant Edit Notification

  Scenario: Edit Notification in Tenant
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "Onexadmin" and password "ali"
#     And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And check Notification is present
    Then click on Notification

    And click on Edit
    And edit data into Notification fields
    And click on Update btn to update

    And Close driver window