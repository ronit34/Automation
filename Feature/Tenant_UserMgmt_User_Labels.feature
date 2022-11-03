Feature: Onextel Tenant User Management Labels
  Scenario: Login to Onextel Tenant Dashboard

        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Click on Sign in Button

        Then click on User_Management
        And click on User tab
        And check if  User Name text is present or not
        And check if  First Name text is present or not
        And check if  Last Name text is present or not
        And check if  Email text is present or not
        And check if  Mobile Number text is present or not
        And check if  Company Name text is present or not
        And check if  Role Type text is present or not
        And check if  Action text inside the user tab is present or not
        And click on the add user inside the user tab
        And check if  Create User text inside the user tab is present or not
        And check if  User Info text inside the user tab is present or not
        And check if  User Name* text inside the user tab is present or not
        And check if  Password* text inside the user tab is present or not
        And check if  First Name* text inside the user tab is present or not
        And check if  Last Name* text inside the user tab is present or not
        And check if  Email* text inside the user tab is present or not
        And check if  Mobile Number* text inside the user tab is present or not
        And check if  Company Name* text inside the user tab is present or not
        And check if  Web* text inside the user tab is present or not
        And check if  Other Mobile Number text inside the user tab is present or not
        And check if  Role Type* text inside the user tab is present or not

        And Close driver window




