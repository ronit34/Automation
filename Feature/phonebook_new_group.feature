Feature: phonebook new group

    Scenario: new group
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
        Then click on phonebook
        And click on Add group
        And enter group data

        And click on contact
        And click on the Add contacts tab
        And select the Upload Bulk Contact option inside add contacts tab
        And choose the contacts file to upload
        And select the group
        And finally click on add button

        And Close driver window
