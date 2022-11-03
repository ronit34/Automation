Feature: DLT Entity ID masking

  Scenario: DLT Entity ids masking
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "AxisUser" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    Then click on DLT
    And Click on Add Entity button
    And Insert data into entity fields
    And click on add button to add entity
    And check entity id created with 3 digits

    And Click on Add Entity button
    And Insert data into entity fields (more than 3 digits)
    And click on add button to add entity
    And check entity id is masked or not

      ##################  check in  sender ID #############################
    And click on Add sender id button
    And Enter Id "123456"
    And Select Entity Name "OneTech(12**56)"
    And Click on Add
    And check entityID masked in created senderID


      ##############  check in template ##############################

    Then click on template
    And click on Add template id button
    And Enter the data into templateid fields(masking)
    And Click on template Add

  ##########################  Bulk Upload ############################
    Then Click on Bulk Upload
    And select masked EntityID in bulk upload
    And select operator in bulk upload
    And select file in bulk upload
    Then Click on save template
    Then Click on okay button to save temp
    And check masked entityID after bulk upload

  #####################   search verify ##############################
    And go to search tab
    And input template Name
    And select template name from dd
    And click on search in dlt search tab
    And check masked entityID in search tab

    And Close driver window





