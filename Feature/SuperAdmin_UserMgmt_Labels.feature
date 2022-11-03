Feature: validate user management text

  Scenario: Login to Onextel localhost and validate user management
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "onexsa" and password "onexsa"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

        And click on user management tab
        And click on tenants tab

        And check if user management text is present or not
        And check if Super Admin text is present or not
        And check if Platform (1) text is present or not

        And check if Tenant Name text is present or not
        And check if TeleMarketer ID text is present or not
        And check if Description text is present or not
        And check if Action text is present or not in user management tab

        And click on add tenant button in usermanagement tab
        And check if Tenant Info text is present or not
        And check if Tenant Name text inside add tenant is present or not
#        And check if TeleMarketer ID text inside add tenant is present or not
        And check if Description text inside add tenant is present or not

        And check if Licenses text is present or not
        And check if Child TUC text is present or not
        And check if SMPPS text is present or not
        And check if SMS API text is present or not
        And check if Create button text is present or not
        And click on cancel button in user management tab

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























