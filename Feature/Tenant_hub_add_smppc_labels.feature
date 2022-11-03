Feature: Hub ADD SMPPC LABELS

    Scenario: Labels
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "Onexadmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And Click on hub
        And click on SMPPC
        And click on add smppc

        And check text of Name*
        And check text of  add smppc Carrier Name*
        And check text of smppc Vendor name

        And check text of add smppc account type
        And check text of  add smppc Circle Name*
        And check text of Gateway Id*

        And check text of SMPP LoginId*
        And check text of System ID*
        And check text of Password*

        And check text of Primary Host/IP*
        And check text of Secondary Host/IP
        And check text of Port*

        And check text of SMS Cost*
        And check text of TPS*
        And check text of no of binds

        And check text of Smppc auto bind
        And check text of Supports Flash*
        And check text of SMPP Bind Type*

        And check text of SMPPC Remarks

        And check text of SMPPC Create
#        And check text of sms charge type
#        And check text of dlt charge type
        And click on cancel of add smppc

        And Close driver window
