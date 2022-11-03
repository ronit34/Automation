Feature: DLT Multiple SenderID

    Scenario: create Multiple SenderID
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        And click on Add sender id button
        And create multiple senderid

        And Close driver window