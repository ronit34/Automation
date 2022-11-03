Feature: option carrier edit

    Scenario: carrier_edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on option tab
        And click on Circle tab
        And Click on Add Circle Button
#        And Check elements are present in circle
        And enter data into circle
        And click on add button of Options to add entered data
        And check edit button of second circle is present
        And check edit icon mouse hover text - circle
        And click on edit button of second circle is present
        And check elements are present in Edit circle
        And Enter the details into edit circle
        And click on update button of edit circle

        And Close driver window