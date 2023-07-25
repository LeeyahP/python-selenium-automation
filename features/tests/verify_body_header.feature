# Created by leeya at 7/17/2023
Feature: CAP-189

  Scenario:User can shop by category Body
    Given Open main page
    When Click to "Shop by category" - select Body
    Then Verify Body header is shown
