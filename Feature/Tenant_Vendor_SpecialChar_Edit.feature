Feature: option Vendor edit

    Scenario: Vendor_edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on option tab
        And click on Vendor tab
        And check edit button of Vendor is present
        And check edit icon mouse hover text - spl character
        And click on edit button of Vendor
        And check elements are present in Edit Vendor
        And Enter the details to edit into edit Vendor
        And click on update of edit Vendor
#        And check if Telemar contain error label or not
        And verify the updated vendor is created or not

        And Close driver window