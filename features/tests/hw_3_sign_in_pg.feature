# Created by leeya at 4/13/2023
Feature: Logged out user sees Sign In


  Scenario: User can see sign in page when clicking on returns and orders button
    Given Open Amazon Page
    When  Click on Return Orders button
    Then  user is redirected to Sign In page