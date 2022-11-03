Feature: DLT senderID

    Scenario: create DLT senderID
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        And click on Add sender id button
        And Enter Id "987654"
        And Select Entity Name
        And Click on Add

        And check edit icon mouse hover text - SenderID

        And click on edit icon in SenderID
        And change the Entity name
        And Click on Update in edit senderID

        And Close driver window
