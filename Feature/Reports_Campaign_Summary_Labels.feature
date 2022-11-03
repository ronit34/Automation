Feature: Report Campaign Summary Labels

     Scenario: Campaign Summary Labels
          Given launch chrome browser
          When open Onextel Homepage "http://localhost:8000/index"
          Then Enter Username "ICICIAdmin" and password "ali"
          And Check Terms And Conditions Check Box is preselected
          And Click on Sign in Button

          And click on report in left menu

          And click on campaign Summary tab in report
          And click on Search Button in campaign

          And Check for Submitted Credits text in campaign Summary
          And Check for Delivered Credits text in campaign Summary
          And Check for Failed Credits text in campaign Summary
          And Check for Awaited Credits text in campaign Summary
          And Check for TUC ID text in campaign Summary
          And Check for TUC Name text in campaign Summary
          And Check for Campaign Name text in campaign Summary
          And Check for Request Time text in campaign Summary
          And Check for SenderID text in campaign Summary
          And Check for Message text in campaign Summary
          And Check for Submitted/Submitted Credits text in campaign Summary
          And Check for Delivered/Delivered Credits text in campaign Summary
          And Check for Failed/Failed Credits text in campaign Summary
          And Check for Awaited/Awaited Credits text in campaign Summary

          And Close driver window