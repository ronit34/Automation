Feature: Tenant Hub Labels

    Scenario: Hub Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        And Click on hub
        And check text of Gateway Name
        And check text of Gateway Description
        And check text of Gateway Carrier Name
        And check text of Gateway Circle Name
        And check text of Gateway Action
        And check text of Gateway +Add Gateway
        And click on SMPPC
        And check text of SMPPC
        And check text of SMPPC Name/Carrier/Vendor/AccountType/Circle
        And check text of SMPPC Gateway id
        And check text of SMPPC TPS
        And check text of SMPPC Binds
        And check text of SMPPC Action
        And check text of SMPPC +Add SMPPC
        And click on Routing
        And check text of Routing
        And check text of +Add Routing
        And click on  Default Gateway
        And check text of Default Gateway
        And check text of Default Gateway OTP*
        And check text of Default Gateway Service Implicit*
        And check text of Default Gateway Service Explicit*
        And check text of Default Gateway Promotional*
        And check text of Default Gateway TransPromo*
        And check text of Default Gateway Government Exempted*
        And check text of Default Gateway Simroute*
        And check text of Default Gateway Save Default Gateways

        And Close driver window








