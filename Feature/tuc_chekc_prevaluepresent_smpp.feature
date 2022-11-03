Feature: Tuc Pre Value Check for SMPP And SMS API

    Scenario: :
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on User_Management
        And Click on Add Tenant Button
        And check smpp assign to zero
        And check SMS API assign to zero
        And clear SMPP value
        And clear SMS API Value

        And Close driver window