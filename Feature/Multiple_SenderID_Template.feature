Feature: Template using multiple sender id

    Scenario: Multiple SenderID template
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on DLT
        Then click on template
        And click on Add template id button
        And check elements is present on the template page
        And Enter data to create new template
        And Click on template Add
        And Check new template is created or not

        And Close driver window