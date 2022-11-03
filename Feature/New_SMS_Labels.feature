Feature: TUC New SMS label check

    Scenario: tuc_label_check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#   Then Check if the message invalid login then close the browser
        And click on new sms
        And check if New SMS text is present or not
        And check if Choose SMS Type text is present or not
        And check if Quick English SMS text is present or not
        And check if Quick Unicode/Multilingual SMS text is present or not
        And check if Dynamic SMS text is present or not
        And check if Campaign SMS text is present or not

        And Close driver window
