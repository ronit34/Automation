Feature: Tenant options add type

    Scenario: add type
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on Options button
        And Click on type
        And Click on add type
        And check text of Add Type
        And check text of Type in Atom
        And check text of Type Name
        And check text of add Type Description
        And check text of Type Add
        And check text Cancel of add Type

        And Close driver window