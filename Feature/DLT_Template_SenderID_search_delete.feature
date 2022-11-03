Feature: DLT Template SenderID Search Delete

  Scenario: Template Sender ID Search Delete
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right Username "ICICIAdmin" and password "ali"
    And Click on Sign in Button
    Then click on DLT
    And Click on Add Entity button
    And Enter Data to create Entity
    And click on add button to add entity
    And click on sender ids tab
    And click on Add sender id button
    And Enter Sender Id "987654"
    And Select the Entity Name
    And Click on Add
    And click on template tab
    And click on Add template id button
    And Enter data to create template
    And Click on template Add
    And input senderID in template to search
    And click on delete template
    And click on sender ids tab
    And click on delete of sender id
    And click on entity tab
    And click on delete of entity id

    And Close driver window
