Feature: Tenant search filters check

  Scenario: TA search tab filters
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "Onexadmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button

    And Click on User_Management
    And click on Search Tab in DLT
# ***************************** For different types of input ****************************
    And input SenderID
    And click on search and check if data is present

    And input SystemID
    And click on search and check if data is present SystemID

    And input SMPP ID
    And click on search and check if data is present SMPP ID

    And input API Key
    And click on search and check if data is present API Key

    And input Tuc ID
    And click on search and check if data is present Tuc ID

    And input User ID
    And click on search and check if data is present User ID

    And Close driver window

