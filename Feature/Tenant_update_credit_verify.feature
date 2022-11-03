Feature: Tenant credit check

  Scenario: Tenant update credits to child cross check

    Given Launch Chrome Browser
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "Onexadmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    Then click on User_Management
    And Check the Available Credits
#    And verify the Available Credits in Credits tab

    And Close driver window


