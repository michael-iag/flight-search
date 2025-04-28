# Feature: Flight Search Functionality
# This feature covers the core functionality of searching for flights based on different criteria.

Feature: Flight Search
  As a user,
  I want to search for flights
  So that I can find suitable travel options.

  @sanity @critical
  Scenario: Search for flights by origin and destination
    Given the flight search system is initialized
    When I search for flights from "NYC" to "LAX"
    Then I should find 2 flights
    And flight "FL001" should be in the results
    And flight "FL005" should be in the results

  @sanity
  Scenario: Search for flights by origin only
    Given the flight search system is initialized
    When I search for flights from "NYC"
    Then I should find 3 flights

  @critical
  Scenario: Search for flights by destination only
    Given the flight search system is initialized
    When I search for flights to "MIA"
    Then I should find 1 flight

  @edgecase
  Scenario: Search for flights with a maximum price
    Given the flight search system is initialized
    When I search for flights from "NYC" to "LAX" with a maximum price of 400.0
    Then I should find 1 flight
    And flight "FL001" should be in the results

  @sanity @critical
  Scenario: Search for flights with no matching criteria
    Given the flight search system is initialized
    When I search for flights from "SFO" to "JFK"
    Then I should find 0 flights

  @negative
  Scenario: Check availability for a specific flight
    Given the flight search system is initialized
    When I check the availability for flight "FL001"
    Then the flight should be available
    When I check the availability for flight "FL005"
    Then the flight should not be available

  @sanity
  Scenario: Get details for a specific flight
    Given the flight search system is initialized
    When I get the details for flight "FL003"
    Then the flight origin should be "CHI"
    And the flight destination should be "MIA"
    And the flight price should be 280.0

