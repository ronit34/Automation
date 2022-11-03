Feature: Config Black List Category

    Scenario:  check Config Black List Category
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Config
#        And click on Black List Category
        And check new blacklist button is present
        And click on new blacklist button
        And check all elements of blak list catefgory is present
        And insert blak list catefgory data
        And click on add button of the given page

        And Close driver window