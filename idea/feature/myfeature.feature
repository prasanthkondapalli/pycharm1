Feature: Ramen application logo
  Scenario: to check the logo present in the home screen
    Given launch chrome browser
    When open application
    Then check the logo of the application
    And close the browser