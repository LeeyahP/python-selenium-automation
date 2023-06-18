# Created by leeya at 5/8/2023
Feature: User can add product to shopping cart


  Scenario: Verify product is added to cart
    Given Open Amazon Page
    When Search for dress
    And Click search button
    And Click on product
    And Store product name
    And Select size
    And Add product to cart
    Then Verify cart has 1 item
    When Open cart page
    Then Validate cart has correct item

