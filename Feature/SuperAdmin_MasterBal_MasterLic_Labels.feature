Feature: validate master balance and master license text

  Scenario: Login to Onextel localhost and validate master balance and master license text
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "onexsa" and password "onexsa"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on master balance tab
        And check if text Master Balance is present or not
#        And check if text Current Balance is present or not
        And check if text Current Credits is present or not
        And click on Super Admin History tab
        And check if From text is present or not
        And check if To text is present or not
        And click on master licence tab
        And check if Master License text is present or not
        And check if License text is present or not
        And check if Total text is present or not
        And check if Used text is present or not
        And check if Available text is present or not
        And check if Action text in master license is present or not

        And Close driver window
