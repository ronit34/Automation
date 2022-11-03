Feature: Config WhiteList Category Delete

    Scenario: Config WhiteList Category delete
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        Then click on Config
        And click on White List Category
        And check delete icon mouse hover text - category_whitelist
        And CLick on delete of created whitelist category
        And Check Message of delete pop up of whitelist category
        And Click on delete button to delete whitelist category
        And Check selected whitelist category is deleted or not

        And Close driver window
