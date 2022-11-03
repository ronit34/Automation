Feature:  Same Name Campaign Validation

    Scenario: : Campaign Validation
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Campaign
        And click on add campaign
        And Enter Name "RCF"
        And Enter Description "It is a NGO"
        Then click on Add Campaign button to create
        And Check for error message in add campaign pop up
        And Close driver window
