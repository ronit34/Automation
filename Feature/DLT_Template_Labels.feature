Feature: validate dlt text

    Scenario: Login to Onextel localhost and validate DLT tabs
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And check DLT is present
        Then click on DLT
        And click on template tab
        And check if Template Name text is present or not
        And check if SenderID text is present or not
        And check if EntityID text is present or not
        And check if TemplateID text is present or not
        And check if Content text is present or not in dlt template
        And check if added on text is present or not
        And check if Type text is present or not
        And check if Action text is present or not in dlt template
        And click on add template button
        And check if Add Template text inside add template is present or not
        And check if Template Name text inside add template is present or not
        And check if Template ID text inside add template is present or not
        And check if Select Type text inside add template is present or not
        And check if Select Entity ID text inside add template is present or not
        And check if Select Sender ID text inside add template is present or not
        And check if Description text inside add template is present or not
        And check if Content text inside add template is present or not

        And Close driver window












