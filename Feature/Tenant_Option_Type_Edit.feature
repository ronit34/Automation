Feature: option carrier edit

    Scenario: carrier_edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on option tab
        And click on Type tab
        And check edit button of first Type is present
        And check edit icon mouse hover text - type
        And click on edit button of first Type is present
        And check elements are present in Edit Type
        And Enter the details into edit Type
        And click on update button of edit Type
        And verify the updated Type created or not

        And Close driver window