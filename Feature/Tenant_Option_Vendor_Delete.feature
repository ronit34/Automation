 Feature: option vendor delete

     Scenario: vendor_delete
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on option tab
        And click on Vendor tab
        And check delete icon is present of second Vendor
        And check delete icon mouse hover text - vendor
        And click on delete icon of second Vendor
        And check if popup is appear inside Vendor tab
        And click on delete button inside Vendor tab
        And verify the vendor is deleted or not

        And Close driver window