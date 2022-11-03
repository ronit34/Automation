Feature: Report Mis complete check

  Scenario: Total complete check MIS
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/index"
    Then Enter Username "ICICIAdmin" and password "ali"
    And Check Terms And Conditions Check Box is preselected
    And Click on Sign in Button
    And click on report in left menu
    And click on search in MIS tab
    ##################################
    And click on the total mis counts
    And fill Wrong Sender ID
    And click on the total mis counts
    And fill Correct Sender ID
    And set limit and check pagination
    ###########################   WEB DETAIL  #####################
    And click on action icon
    And verify submitted count
    And enter mobile number
    And click on search in web detail
    And verify submitted count
    And check for zero count
    ########################## STATUS CHECK ########################
    And select Status(Delivered)
    And click on search in web detail
    And verify submitted count
    And select Status(Failed)
    And click on search in web detail
    And verify submitted count
    And select Status (Awaited)
    And click on search in web detail
    And verify submitted count
    And set status to all

    #############################  DOWNLOAD FILE ####################
    And click the Download Button in MIS Report
    And select Download file type in action
    And Click on okay in pop up
    And click on download data
    And click on download icon

    And Close driver window

