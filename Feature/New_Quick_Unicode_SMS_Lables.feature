Feature: TUC label check

    Scenario: tuc_label_check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on new sms button
        And click on Quick Unicode/Multilingual SMS
        And check if New SMS/Unicode SMS text is present or not
        And check if Campaign Name text is present or not in quick sms
        And check if Sender ID text is present or not in quick sms
        And click on sender id search box and select the first option in quick sms
        And check if Recipients text is present or not in quick sms
        And Enter valid number in Recipients text field
        And check if Select Group/s text is present or not in quick sms
        And check if clear text is present or not in quick sms
        And check if Remove Duplicate Numbers text is present or not in quick sms
        And check if Remove Invalid Numbers text is present or not in quick sms
        And check if Content text is present or not in quick sms
        And click on insert template button in quick sms
        And check if Insert Template text  is present or not in quick sms
        And check if Select Template Type text  is present or not in quick sms
        And select the template type from Select Template Type dropdown
        And check if Select Template text  is present or not in quick sms
        And select unicode template from Select Template dropdown
        And check if Template ID text  is present or not in quick sms
        And check if Parameter text  is present or not in quick sms
        And check if Template content text  is present or not in quick sms
        And click on select button inside insert template button in quick sms
        And click on Insert Url text
        And check if Insert Url text is present or not in quick sms
        And check if select domain text is present or not in quick sms
        And check if Target Url text is present or not in quick sms
        And click on the Cancel Url button
        And check if clear text second is present or not in quick sms
        And check if Save as Template text is present or not in quick sms
        And check if Allow Multi Part SMS text is present or not in quick sms
        And select the Allow Multi Part SMS checkbox
        And check if Allow Unicode text is present or not in quick sms
        And select the Allow Unicode checkbox
        And check if Send as Flash SMS text is present or not in quick sms
        And check if Schedule SMS text is present or not in quick sms
        And check if cancel text is present or not in quick sms
        And check if send text is present or not in quick sms
        And click on the send button

        And check the sms confirmation text
        And check sender id text is present or not inside send button
        And check the Message text is present or not inside send button
        And check if Invalid Numbers text is present or not inside send button
        And check if Duplicate Number text is present or not inside send button
        And check if Valid Numbers text is present or not inside send button
        And check if SMS Character Count is present or not inside send button
        And check if Total Required SMS Credits text is present or not inside send button
        And check if Schedule Time text is present or not inside send button
        And click on cancel button inside send button
        And click on view schedule tab in quick sms
        And check the  text of view schedule tab in quick sms
        And check if Sender ID text is present inside view schedule tab or not in quick sms
        And check if Scheduled Date Time text is present or not in quick sms
        And check if Message text is present or not in quick sms
        And check if Valid Numbers text is present or not in quick sms
#        And check if Template Length text is present or not in quick sms
        And check if Message Length text is present or not in quick sms
        And check if Total Credits text is present or not in quick sms
        And check if Status text is present or not in quick sms
        And check if Action text is present or not in quick sms

        And Close driver window