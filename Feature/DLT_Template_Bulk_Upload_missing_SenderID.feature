Feature: DLT Bulk Upload

    Scenario: DLT Bulk Upload Files
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        Then Click on Bulk Upload
        Then Select Entity Id
        Then Select bsnl operator
        And choose file for bsnl
        Then Click on save template
        And check senderid Field missing popup
        Then click on OK button in bulk upload
        And close browser