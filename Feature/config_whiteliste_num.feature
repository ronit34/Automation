Feature: Config White List Number

    Scenario:  check Config White List num
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Config
        And click on white list number
        And check add White list number elements is present
        And Check add White list label is present

        And Close driver window