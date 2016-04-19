Feature: Finding web page
  In order to find web page with unknown url address,
  As a normal user
  I want to find it through search field


  Scenario: I want to find www.seznam.cz
    Given a search phrase www.seznam.cz
    When user navigates to google.com
    And fill in the input with phrase
    Then google.com will find seznam.cz