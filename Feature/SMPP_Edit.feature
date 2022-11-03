Feature: SMPP scrub dnd checkbox

    Scenario: SMPP
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check SMPP is present
        And click on SMPP

        And click on edit icon in smpp
        And change the values in fields


        And check DND_Filter is deselected or not

        And click on update button in SMPPS
        And check SMPP is edited or not
        And close browser