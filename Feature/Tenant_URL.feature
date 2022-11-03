Feature: Tenant URL

    Scenario: Tenant URL and labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on URL of tenant
        And Check text of  url tenant
        And Check text of  status tenant
        And Check text of  action tenant
        And click on add short URl button to add URL
        And enter url of tenant
        And click on ad
        And click on add short URl button to add URL
        And enter new url of tenant
        And click on ad
        And Check entered URL is created or not

        And Close driver window
