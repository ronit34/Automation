Feature:HDFC DLT senderID

    Scenario: create DLT senderID
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "HDFCAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        And click on Add sender id button
        And check elements is present on page
        And Enter Id "123456"
        And Select Entity Name "Onextel(123)"
        And Click on Add

        And Close driver window