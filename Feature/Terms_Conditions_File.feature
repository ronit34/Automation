Feature: Terms and Conditions File

    Scenario: Terms and Conditions check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"

        And Check Terms and Conditions text
        Then Click on Terms and Conditions text

        And check for Terms and Conditions header on New Page
        And check for User Eligibility text on New Page
        And check for Scope of Terms and Conditions text on New Page
        And check for Modifications text on New Page
        And check for Privacy Notice text on New Page
        And check for Licence and Ownership text on New Page
        And check for System and Network Security text on New Page

        And Close driver window















