Feature: Campaign summary download file and verify file is empty or not

  Scenario: Campaign summary download file and verify file is empty or not
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "ICICIAdmin" and password "ali"
        And Click on Sign in Button
        And Click on Report
        And Click on Campaign Summary
        And Click on Search in campaign summary
        And Click on Download in csv file
        And Click on Download csv file pop-up
        And Click on Download Data for campaign summary file check
        And Click on Download button in download data
        And Open downloaded file and verify empty or not
        And Close Windows Driver
