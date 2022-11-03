Feature: DLT_charge_type_on_delivery

    Scenario: : Account on delivery
        ##### Creating TUC #####
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "AxisUser" and password "ali"
        And Click on Sign in Button
        And Click on User_Management
        And Click on Add Tenant Button

        And insert lss cost and check error label
        And click on create button to save it
        And check error label of cost

        And update cost
        And click on create button to save it

        And Close driver window