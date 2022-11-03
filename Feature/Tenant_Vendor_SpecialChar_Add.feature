Feature: option Vendor add

    Scenario: Vendor_add
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on option tab
        And click on Vendor tab
        And check add button of Vendor is present
        And click on add button of  Vendor
        And check elements are present in Add Vendor
        And Enter the details into add Vendor
        And click on Add button of add Vendor
        And check if TelemarID contain error label or not
#        And verify the vendor created or not

        And Close driver window