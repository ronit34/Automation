Feature: Config ADD Black List Number

    Scenario:  Config add Black List num
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Config
        And click on Black List Number
        And check add black list number elements is present
        And Check add blak list label is present

        And Close driver window