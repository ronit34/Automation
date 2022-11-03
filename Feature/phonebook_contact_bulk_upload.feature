Feature: bulk upload contact

    Scenario: bulk upload
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#     And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#    Then Check if the message invalid login then close the browser
        And check phonebook is present
        Then click on phonebook
        And click on contact
        And click on the Add contacts tab
        And select the Upload Bulk Contact option inside add contacts tab
        And choose the file to upload
        And select the group to which you want to add contacts
        And finally click on add button

        And Close driver window