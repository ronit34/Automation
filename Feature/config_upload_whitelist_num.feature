Feature: TUC config upload blacklist number

  Scenario: Login to onextel and upload blacklist number
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Right username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    Then click on Config
    And click on white list number
    And click on Upload Whitelist Number tab
    And click on Choose a File for whitelist upload
#    And select category Whitelist
#    Then click on Upload button

     And Close driver window


