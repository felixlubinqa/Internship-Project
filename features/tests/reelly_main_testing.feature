# Created by felix at 4/22/2025
Feature: Main Testing Page
  # Enter feature description here

  Scenario: User can open market tab and filter by developers option
    Given Open the main page
    When Enter username
    And Type password
    And Log in to the page
    When Click on 'market' on the left side menu
    Then Verify the right page opens
    When Click on Developers filter at the top of the page
    Then Verify all cards have the license tag