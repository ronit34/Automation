Feature: Edit campaign

    Scenario: : edit steps
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Campaign
        And click on add campaign
        And Enter Name "Test"
        And Enter Description "It's a test campaign"
        Then click on Add Campaign button to create
        And check edit icon is present in campaign
        And check edit icon mouse hover text - campaign

        And click on campaign edit icon
        And check elements are present in Edit icon of campaign
        And Enter the details into edit icon of campaign
        And click on update button of edit icon
        And check  campaign name is updated or not
        And check  description is updated or not

        And Close driver window