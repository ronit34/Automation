Feature: check tenant dashboard label

    Scenario: Tenant_Dashboard_Label_check
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Check Terms And Conditions Check Box is preselected
        And Click on Sign in Button

        And click on DLT Management
        And check if DLT text is present or not

        And go to dashboard

        And click on Schedule campaigns quick stats
        And verify redirected page in reports

        And go to dashboard

        And click on sender id quick stats
        And check if Sender ID text is present or not in dlt sender id tab

        And go to dashboard

        And click on template quick stats
        And verify redirected template tab heading

        And go to dashboard

        And click on contacts quick shortcut
        And verify redirected to contacts tab

        And go to dashboard

        And click on groups quick shortcut
        And verify redirected to groups tab


        And go to dashboard

        And check whether No Scheduled Record Found text is present in Scheduled SMS

        And Close driver window








