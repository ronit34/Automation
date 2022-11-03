Feature: DLT templateID

    Scenario: create DLT templateID
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT

        Then click on template
         And click on Add template id button
        And Enter data to create 1st temp1
        And Click on template Add

#        And click on Add template id button
#        And Enter data to create second temp2
#        And Click on template Add

        And check edit icon mouse hover text - template

        And click on edit icon in temp1
        And change the field data
        And click on update to save changes
        And check the updated changes

        And select the check box of the template
        And Click on Delete Selected button
        And Click on the Delete button of Delete Selected popup

        And Close driver window




