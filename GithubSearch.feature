Feature: Github Search

  Background:
    Given Navigate to https://gh-users-search.netlify.app
    When UI: search for <username>

  Scenario: verify total number of Repos against API
    And GitHub Integration API: verify total number of Repos
    Then Print Results

  Scenario: verify number of followers against API
    And API: send GET request to users/<username>/followers?per_page=100
    And API: verify status code is 200
    Then GitHub Interaction API: verify total number of followers

  Scenario: verify number of following against API
    And API: send GET request to users/<username>/following?per_page=100
    And API: verify status code is 200
    Then GitHub Interaction API: verify total number of following

  Scenario: verify number of gists against API
    And API: send GET request to users/<username>/gists?per_page=100
    And API: verify status code is 200
    Then GitHub Interaction API: verify total number of gists

  Scenario: verify user's full name against API
    And API: send GET request to users/<username>
    And API: verify status code is 200
    Then GitHub Interaction API: verify user's full name

  Scenario: verify user's twitter against API
    And API: send GET request to users/<username>
    And API: verify status code is 200
    Then GitHub Interaction API: verify user's twitter

  Scenario: verify user's bio against API
    And API: send GET request to users/<username>
    And API: verify status code is 200
    Then GitHub Interaction API: verify user's bio

  Scenario: verify user's company name against API
    And API: send GET request to users/<username>
    And API: verify status code is 200
    Then GitHub Interaction API: verify user's company name

  Scenario: verify user's location against API
    And API: send GET request to users/<username>
    And API: verify status code is 200
    Then GitHub Interaction API: verify user's location

  Scenario: verify user's blog against API
    And API: send GET request to users/<username>
    And API: verify status code is 200
    Then GitHub Interaction API: verify user's blog

  Scenario: verify follow button redirect against API
    And API: send GET request to users/<username>
    And API: verify status code is 200
    Then GitHub Interaction API: verify follow button redirect

  Scenario: verify followers component against API
    And API: send GET request to users/<username>/followers?per_page=100
    And API: verify status code is 200
    Then GitHub Interaction API: verify follower data