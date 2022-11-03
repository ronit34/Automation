Feature: DLT Delete Select

    Scenario: DLT Delete Select
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
        And Click on Sign in Button
        Then click on DLT
        And click on Bulk Upload tab
        And Select Entity ID from Entity ID dropdown
        And Select Operator from Operator dropdown
        And Choose file from Choose file option
        And Click on Save Template button
        And Click on the ok button of Message popup
        And Select all the files of that group
        And Click on Delete Selected button
        And Click on the Delete button of Delete Selected popup

        And Close driver window