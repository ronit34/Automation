Feature: Onextel reports user login

  Scenario: Login to Onextel   reports labels localhost
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on the smpp tab
        And check if SMPP header text is present or not

        And check if the text of SMPP is present or not

        And check if the text of SMPP ID text is present or not
        And check if System ID/User ID text is present or not
        And check if Account Type text is present or not in smpp tab
        And check if SMPP Bind Type text is present or not
        And check if IP Address text is present or not in smpp tab
        And check if Action text is present or not in smpp tab

        And click on add smpp button
        And check if Create SMPP text is present or not
        And check if SMPP Account text is present or not

        And check if System ID/User ID* text is present or not
        And check if Password* text is present or not
        And check if System Type* text is present or not
        And check if Account Type* text is present or not
        And check if Limit SMS / Day* text is present or not
        And check if Limit SMS / Hour* text is present or not
        And check if Validity* text is present or not
        And check if SMPP Bind Type* text is present or not
        And check if IP Address text inside add smpp is present or not
        And check if TLV Template ID text is present or not
        And check if TLV Entity ID text is present or not
        And check if Total TPS* text is present or not
        And check if Keep Alive* text is present or not
        And check if Max Binds* text is present or not
        And check if Other text is present or not
        And check if DND_filter text is present or not
#        And check if Active text is present or not
#        And check if Forced_DLR text is present or not
#        And check if Credit_Rollback text is present or not
        And check if Check_Time text is present or not
        And check the text of create button
        And check the text of cancel button and click on it if it is present in smpp tab

        And check the text of bind history button and click on it if it is present
        And check if IP text is present or not
        And check if Bind/Unbind text is present or not
        And check if DateTime text is present or not

        And Close driver window
