Feature: TUC label check

    Scenario: tuc_label_check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms button
        And click on Campaign SMS
        And check if New SMS/Campaign SMS text is present or not
        And check campaign sms tab text
        And click on the choose file in Campaign SMS tab
        And check if Campaign Name text is present or not
        And check if Sender ID text is present or not
        And click on sender id search box and select the first option

        And check if Remove Duplicate Numbers text is present or not
        And check if Remove Invalid Numbers text is present or not
        And check if Content text is present or not

        And click on insert template button in dynamic sms
        And check if Insert Template text  is present or not in dynamic sms
        And check if Select Template Type text  is present or not in dynamic sms
        And select the template type from Select Template Type dropdown

        And check if Select Template text  is present or not in dynamic sms
        And select template from Select Template dropdown
        And check if Template ID text  is present or not in dynamic sms
        And check if Parameter text  is present or not in dynamic sms
        And check if Template content text  is present or not in dynamic sms
        And click on select button inside insert template button in quick sms

        And check if clear text second is present or not in dynamic sms
        And check if Save as Template text is present or not
        And check if Allow Multi Part SMS text is present or not
        And select the Allow Multi Part SMS checkbox in campaign sms
        And check if Allow Unicode text is present or not
        And check if Send as Flash SMS text is present or not
        And check if Schedule SMS text is present or not
        And check if cancel text is present or not
        And check if Save as Draft text is present or not
        And check if send text is present or not
        And click on send button

        And check the SMS Confirmation text inside send button is present or not
        And check the Sender ID text inside send button is present or not
        And check the Message text inside send button is present or not
        And check the Invalid Numbers text inside send button is present or not in campaign sms
        And check the Duplicate Numbers text inside send button is present or not
        And check the DND Numbers text inside send button of campaign is present or not
        And check the Blacklisted Numbers text inside send button of campaign is present or not
        And check the Valid Numbers inside send button is present or not in campaign sms
        And check the SMS Character Count text inside send button is present or not in campaign sms
        And Total Required SMS Credits text inside sender button is present or not in campaign sms
        And Schedule Time text inside send button is present or not in campaign sms
#        And Total Balance Required text inside send button is present or not in campaign sms
        And click on cancel button inside send button in dynamic sms

        And click on view schedule tab in dynamic sms
        And check the  text of view schedule tab in quick sms
        And check if Sender ID text is present inside view schedule tab or not
        And check if Scheduled Date Time text is present or not
        And check if Message text is present or not
        And check if Valid Numbers text is present or not
#        And check if Template Length text is present or not
        And check if Message Length text is present or not
        And check if Total Credits text is present or not
        And check if Status text is present or not
        And check if Action text is present or not

        And Close driver window
