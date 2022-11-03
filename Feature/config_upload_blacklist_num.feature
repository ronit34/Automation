Feature: TUC config upload blacklist number

  Scenario: Login to onextel and upload blacklist number
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    Then click on Config
    And click on Black List Number
    And click on Upload Blacklist Number
    And click on Choose a File
#    And select category Blacklist
#    Then click on Upload button

     And Close driver window
