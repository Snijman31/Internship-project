# Created by sarah-annnijman at 1/16/25
Feature:


  Scenario: User can go to settings and see the right numb
    Given Open main page https://soft.reelly.io/sign-in
    When Log in to the page
    And Click on settings option
    And Verify the right page opens
    Then Verify there are 13 options for the settings
    Then Verify “connect the company” button is available