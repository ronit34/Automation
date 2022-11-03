Feature: Config Black List Category Delete

    Scenario: Config Black List Category delete
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Config
        And check delete icon mouse hover text - blacklist_category
        And CLick on delete of created blacklist category
        And Check Message of delete pop up
        And Click on delete button to delete category
        And Check selected blacklist category is deleted or not

        And Close driver window
