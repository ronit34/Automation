Feature: TUC User Management update credit

    Scenario: Tuc add credits to child
        Given Launch Chrome Browser
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on User_Management
        And Check the Available Credits
#        And click on Manage Credit icon
#        And Enter the Amount "100"
#        And Select Add-Credit
#        Then Click on update to add credits
#
#        And check Updated credit

         And Close driver window



