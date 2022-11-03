Feature: check for the text of the user profile in super admin

  Scenario: Login to Onextel localhost and check for the text of the user account in super admin
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "onexsa" and password "onexsa"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on super admin after which drop down menu will appear

        And now click on the my account option of the drop down menu
        And check if User Settings text is present or not
        And check if Profile Details text is present or not
        And check if First Name text is present or not
        And check if Last Name text is present or not
        And check if Company text is present or not
        And check if Email text is present or not
        And check if Phone No text is present or not
        And check if Save Changes text is present or not

        And click on alert tab
#        And check if SMS Report Alerts text is present or not
#        And check if Daily Usage text is present or not
#        And check if Weekly Usage text is present or not
#        And check if Monthly Day-wise Usage text is present or not
#        And check if Credit Alerts text is present or not
#        And check if Low Balance alert by SMS text is present or not
#        And check if Low Balance alert by Email text is present or not
        And check if Low Credit alert by Email text is present or not
#        And check if Weekly Transaction Report text is present or not
#        And check if Monthly Transaction Report text is present or not

        And click on change password tab
        And check if Current Password text is present or not
        And check if New Password text is present or not
        And check if Re-enter Password text is present or not
        And check if Submit Request text is present or not

        And click on Login History tab
        And check if IP Address text is present or not
        And check if Login Time text is present or not

        And Close driver window