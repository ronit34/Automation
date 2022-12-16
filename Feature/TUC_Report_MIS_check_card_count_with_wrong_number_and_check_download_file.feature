Feature: Campaign summary download file and verify file is empty or not

  Scenario: Campaign summary download file and verify file is empty or not
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Right username "ICICIAdmin" and password "ali"
        And Click on Sign in Button
        And Click on Report
        And Click on Total Number of MIS
        And Enter Wrong Number and Search
        And Verify Card Count
        And Click on Download All
        And Click on Download data
        And Click on download button in download data
        And Verify file is empty or not
        And Close Window Driver
