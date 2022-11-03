Feature: SenderID to Multiple EntityID

  Scenario: Allocation of single senderid to multiple entity id
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "ICICIAdmin" and password "ali"
    And Click on Sign in Button
    Then click on DLT
    And Click on Add Entity button
    And Enter Data to create new Entity
    And click on add button to add entity
    And click on sender ids tab
    And click on Add sender id button
    And Enter New Sender Id "123456"
    And Select new Entity Name
    And Click on Add button to add sender id
    And Check for Error Message

    And Close driver window