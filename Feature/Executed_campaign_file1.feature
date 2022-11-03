Feature: DLT senderID

    Scenario: create DLT senderID
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        Then click on DLT
        And click on Add sender id button
        And Enter Id "098765"
        And Select Entity Name "Onextel(123)"
        And Click on Add

        Then click on template
        And click on Add template id button
        And Enter data to template fields
        And Click on template Add

         And click on new sms
        And click on quick sms
        And insert data to schedule quick sms

        And Schedule sms
        And click on send button
        And click on send now button of dynamic sms
        And click on View Schedule
        And check sms scheduled for execution

        And Close driver window




