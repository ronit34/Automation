Feature: check tenant dashboard label

    Scenario: Tenant_Dashboard_Label_check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser

#        And check if Filter label is present
#        And check whether Not able to load data! text is present
        And Check text of Dashboard header
        And Check text of Today in graph
        And Check text of Week in graph
        And Check text of Month in graph

        And check whether No Scheduled Record Found text is present in Scheduled SMS

        And Check text of Today
        And Check text of Week
        And Check text of Month

        And Check text of Quick Stats
        And Check text of Schedule Campaigns
        And Check text of Inactive Accounts
        And Close driver window

