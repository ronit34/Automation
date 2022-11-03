Feature: option carrier edit

    Scenario: carrier_edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on option tab
        And Click on Add Carrier
        And enter data to add Carrier
        And click on add button of Options to add entered data
        And check edit button of first carrier is present
        And check edit icon mouse hover text - carrier
        And click on edit button of first carrier is present
        And check elements are present in Edit Carrier
        And Enter the details into edit Carrier
        And click on update button of edit Carrier
        And verify the updated Carrier created or not

        And Close driver window










