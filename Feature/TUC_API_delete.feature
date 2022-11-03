Feature: Onextel api Delete

  Scenario: Delete_api
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/index"
        Then Enter Username "ICICIAdmin" and password "ali"
        And Click on Sign in Button
        And click on the api tab
        And check delete icon mouse hover text - API
        And click on the delete icon
        And check whether delete pop is appeared
        And click on the delete button

        And Close driver window