Feature: Onextel Tenant Dashboard
  Scenario: Login to Onextel Tenant Dashboard
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        Then click on User_Management
        And Check label of User Management in header
        And Check for TUC tab
        And Click on Add TUC

        And Check for Add Tenant Customer Logo
        And Check for TUC Info

        And Check for Name
#        And Check for Cost For OTP
#        And Check for Transactional
#        And Check for Cost For Promotional
#        And Check For Cost For Sim Route
#        And Check for Scrubbing Cost Per SMS
#        And Govt SMS Cost
#        And Govt Scrubbing Cost
#        And Check for Cost Unit

        And Check for OTP Charge type
        And Check for Trans Charge type
        And Check for Promo Charge type
        And Check for Govt Charge type
        And Check for SIM Route Charge type
        And Check for Default Charge type

#        And Check for Account Manager
        And Check for Billing Type
#        And Check for DLT Charges Type
#        And Check for SMS Charges Type
        And Check for validity
        And Check for Mask Phone

        And Check for Create Button
        And Check for Cancel Button

        And Check for search in userMgmt
        And Check for reset in userMgmt
        And Check for Download in userMgmt

        And Check for TUC Name in userMgmt
        And Check for Available Credits in userMgmt
        And Check for Validity in userMgmt
        And Check for Status in userMgmt
        And Check for Creation Time in userMgmt
        And Check for Action in userMgmt

        And Close driver window




