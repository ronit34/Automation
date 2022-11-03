Feature: option carrier delete

    Scenario: carrier_delete
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on option tab
        And click on Circle tab
        And check delete icon is present of second circle
        And check delete icon mouse hover text - circle
        And click on delete icon of second circle
        And check if popup is appear inside circle tab
        And click on delete button inside circle tab
        And verify the carrier is deleted or not

        And Close driver window