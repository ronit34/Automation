Feature: Onextel reports user login

  Scenario: Login to Onextel   reports labels localhost
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
#        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button
#        Then Check if the message invalid login then close the browser
        And click on Report

        And check text of Mis under report
        And click on MIS
        And check text of Mis under report TUCs
        And check text of Mis under report Month
        And check text of Mis under report Year
        And check text of Mis under report Search
        And check text of Mis under report Download

        And check text of Summary
        And click on summary tab in report tab
        And check text under report in search TUCs
        And check text under report in search From
        And check text under report in search To
#        And check text under report in search Limit

        And click on campaign summary tab
        And check text TUCs Campaign Summary under report
        And check text From Campaign Summary under report
        And check text To Campaign Summary under report
        And check text Campaign Name Campaign Summary under report
        And check text Limit Campaign Summary under report
        And check text Search Campaign Summary under report
        And check text Download Campaign Summary under report
        And check the text of search tab

        And click on search tab
        And check text TUCs in search tab under report
        And check text From in search tab under report
        And check text To in search tab under report
        And check text Limit in search tab under report
        And check text Mobile in search tab under report
        And check text Sender ID in search tab under report
        And check text UUID in search tab under report
        And check text Source Type in search tab under report
        And check text of Sender ID Summary under report

        And click on Sender ID Summary
        And check text of Sender ID Summary under report TUCs
        And check text of Sender ID Summary under report From
        And check text of Sender ID Summary under report To
        And check text of Sender ID Summary under report Sender ID(optional)
        And check text of Sender ID Summary under report Search

        And check text of Clicker Data
        And click on the Clicker Data tab
        And check text of Clicker Data under report TUCs
        And check text of Clicker Data under report From
        And check text of Clicker Data under report To
        And check text of Clicker Data under report Mobile
#        And check text of Clicker Data under report Campaign Name
        And check text of Clicker Data under report Limit
        And check text of Clicker Data under report Search
        And check  text of Download Data under report

        And click on the Schedule Campaigns tab
        And check text of Schedule Campaigns under report TUCs
        And check text of Schedule Campaigns under report From
        And check text of Schedule Campaigns under report To
        And check text of Schedule Campaigns under report Campaign Name
        And check text of Schedule Campaigns under report Limit
        And check text of Schedule Campaigns under report Search
        And check  text of Download Data under report

        And click on Download Data
        And check  text of Download Data under report Request Time
        And check  text of Download Data under report File Creation Time
        And check  text of Download Data under report Report Type | DocType
        And check  text of Download Data under report File Name
        And check  text of Download Data under report Filters
        And check  text of Download Data under report Status
        And check  text of Download Data under report Download

        And Close driver window