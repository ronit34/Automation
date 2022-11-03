Feature: validate credits text

  Scenario: Login to Onextel localhost and validate credits
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "onexsa" and password "onexsa"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on credits tab
        And check if text credit is present or not
        And check if text Select Tenant/TUC is present or not
        And check if text PID/User is present or not
        And check if text Name/Company is present or not
#        And check if text Amount is present or not
        And check if text Credits is present or not
        And check if text Allocated by is present or not
        And check if text Tr Date/Time is present or not
        And check if text Transaction/Type is present or not
        And check if text Remark is present or not
        And click on all allocation
        And check if text From is present or not
        And check if text To is present or not

        And Close driver window
