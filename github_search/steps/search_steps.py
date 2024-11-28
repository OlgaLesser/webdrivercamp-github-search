from behave import *
from components.base import GitHubAPI
from components.base import GitHubUI
from token_service import get_token


@step('Navigate to {url}')
def step_impl(context, url):
    context.browser.get(url)


@step("UI: search for {username}")
def get_username(context, username=None):
    username = "OlgaLesser"
    context.username = username


@step("GitHub Integration API: verify total number of Repos")
def verify_repo_count(context):
    github_api = GitHubAPI(token=get_token())
    expected_repo_count = github_api.get_repo_count(context.username)
    context.repo_count = expected_repo_count
    github_ui = GitHubUI()
    ui_repo_count = github_ui.get_ui_repo_count(context.username)
    context.ui_repo_count = ui_repo_count


@step("Print Results")
def print_results(context):
    if context.repo_count != context.ui_repo_count:
        print(f"Mismatch: API repos ({context.repo_count}) vs. Web UI ({context.ui_repo_count})")
    else:
        print(f"Repo count matches: API and Web UI ({context.repo_count})")


@step("API: send GET request to {url}")
def send_request(context, url):
    github_api = GitHubAPI(token=get_token())
    request_url = url.replace("<username>", context.username)
    response = github_api.send_request(request_url)
    context.response = response


@step("API: verify status code is 200")
def verify_status_code(context):
    if context.response.status_code != 200:
        raise AssertionError(f"API request failed with status code: {context.response.status_code}")


@step("GitHub Interaction API: verify total number of followers")
def verify_follower_data(context):
    github_ui = GitHubUI()
    data = context.response.json()
    expected_follower_count = len(data)
    ui_follower_count = github_ui.get_ui_follower_count(context.username)
    if expected_follower_count != ui_follower_count:
        print(f"Mismatch: API followers ({expected_follower_count}) vs. Web UI ({ui_follower_count})")
    else:
        print(f"Follower count matches: API and Web UI ({expected_follower_count})")


@step("GitHub Interaction API: verify total number of following")
def verify_following_data(context):
    github_ui = GitHubUI()
    data = context.response.json()
    expected_following_count = len(data)
    ui_following_count = github_ui.get_ui_following_count(context.username)
    if expected_following_count != ui_following_count:
        print(f"Mismatch: API following ({expected_following_count}) vs. Web UI ({ui_following_count})")
    else:
        print(f"Following count matches: API and Web UI ({expected_following_count})")


@step("GitHub Interaction API: verify total number of gists")
def verify_gists_data(context):
    github_ui = GitHubUI()
    data = context.response.json()
    expected_gists_count = len(data)
    ui_gists_count = github_ui.get_ui_gists_count(context.username)
    if expected_gists_count != ui_gists_count:
        print(f"Mismatch: API gists ({expected_gists_count}) vs. Web UI ({ui_gists_count})")
    else:
        print(f"Gists count matches: API and Web UI ({expected_gists_count})")


@step("GitHub Interaction API: verify user's full name")
def verify_full_name(context):
    github_ui = GitHubUI()
    data = context.response.json()
    expected_full_name = data['name']
    ui_full_name = github_ui.get_ui_full_name(context.username)
    if expected_full_name != ui_full_name:
        print(f"Mismatch: API full name ({expected_full_name}) vs. Web UI ({ui_full_name})")
    else:
        print(f"Full name matches: API and Web UI ({expected_full_name})")


@step("GitHub Interaction API: verify user's twitter")
def verify_twitter(context):
    github_ui = GitHubUI()
    data = context.response.json()
    expected_twitter = data['twitter_username']
    ui_twitter = github_ui.get_ui_twitter(context.username)
    if expected_twitter != ui_twitter:
        print(f"Mismatch: API twitter ({expected_twitter}) vs. Web UI ({ui_twitter})")
    else:
        print(f"Twitter matches: API and Web UI ({expected_twitter})")


@step("GitHub Interaction API: verify user's bio")
def verify_bio(context):
    github_ui = GitHubUI()
    data = context.response.json()
    expected_bio = data['bio']
    ui_bio = github_ui.get_ui_bio(context.username)
    if not expected_bio and not ui_bio:
        print("Both API and UI bio are empty or invalid.")
        return
    if expected_bio != ui_bio:
        print(f"Mismatch: API bio ({expected_bio}) vs. Web UI ({ui_bio})")
    else:
        print(f"Bio matches: API and Web UI ({expected_bio})")


@step("GitHub Interaction API: verify user's company name")
def verify_company(context):
    github_ui = GitHubUI()
    data = context.response.json()
    expected_company = data['company']
    ui_company = github_ui.get_ui_company(context.username)
    if not expected_company and not ui_company:
        print("Both API and UI company names are empty or invalid.")
        return
    if expected_company != ui_company:
        print(f"Mismatch: API company name ({expected_company}) vs. Web UI ({ui_company})")
    else:
        print(f"Company name matches: API and Web UI ({expected_company})")


@step("GitHub Interaction API: verify user's location")
def verify_location(context):
    github_ui = GitHubUI()
    data = context.response.json()
    expected_location = data['location']
    ui_location = github_ui.get_ui_location(context.username)
    if not expected_location and not ui_location:
        print("Both API and UI locations are empty or invalid.")
        return
    if expected_location != ui_location:
        print(f"Mismatch: API location ({expected_location}) vs. Web UI ({ui_location})")
    else:
        print(f"Location matches: API and Web UI ({expected_location})")


@step("GitHub Interaction API: verify user's blog")
def verify_blog(context):
    github_ui = GitHubUI()
    data = context.response.json()
    expected_blog = data['blog']
    ui_blog = github_ui.get_ui_blog(context.username)
    if not expected_blog and not ui_blog:
        print("Both API and UI blogs are empty or invalid.")
    elif expected_blog != ui_blog:
        print(f"Mismatch: API blog ({expected_blog}) vs. Web UI ({ui_blog})")
    else:
        print(f"Blog matches: API and Web UI ({expected_blog})")
    if expected_blog:
        github_ui.verify_blog_link(expected_blog)


@step("GitHub Interaction API: verify follow button redirect")
def verify_follow_button(context):
    github_ui = GitHubUI()
    github_ui.test_follow_button_redirect(context.username)


@step("GitHub Interaction API: verify follower data")
def verify_followers(context):
    data = context.response.json()
    github_ui = GitHubUI()
    for follower in data:
        expected_login = follower['login']
        expected_url = follower['html_url']
        github_ui.verify_follower_details(expected_login, expected_url)
