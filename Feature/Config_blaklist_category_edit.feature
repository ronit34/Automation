Feature: Config Black List Category Edit

    Scenario: Config Black List Category edit
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Config
        And check new blacklist button is present
        And click on new blacklist button
        And check all elements of blak list catefgory is present
        And insert black list data
        And click on add button of the given page
        And check edit icon mouse hover text - blacklist_category
        And Click on Edit of the created blacklist category
        And Enter new category name to update
        And Enter new description to update
        And Click on update button to update data

        And Close driver window
