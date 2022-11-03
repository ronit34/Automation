Feature: option carrier delete

    Scenario: carrier_delete
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on option tab
        And check delete icon is present of first carrier
        And check delete icon mouse hover text - carrier
        And click on delete icon of first carrier
        And check if popup is appear or not
        And click on delete button inside carrier tab
        And verify the carrier is deleted or not

        And Close driver window