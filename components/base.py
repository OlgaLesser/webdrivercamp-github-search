import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GitHubAPI:
    def __init__(self, api_url_base="https://api.github.com", token=None):
        self.api_url_base = api_url_base
        self.token = token

    def get_repo_count(self, username):
        headers = {}
        url = f"{self.api_url_base}/users/{username}/repos"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return len(response.json())
        else:
            print(f"Error fetching repository count for {username}: {response.status_code}")
            return None

    def send_request(self, endpoint):
        headers = {}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        url = f"{self.api_url_base}/{endpoint}"
        response = requests.get(url, headers=headers)
        return response


class GitHubUI:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_user_page(self, username):
        self.driver.get(f"https://gh-users-search.netlify.app/")
        search_input = self.driver.find_element(By.XPATH, "//*[@id='root']/main/section[1]/div/form/div/input")
        search_input.click()
        search_input.send_keys(username)
        search_button = self.driver.find_element(By.XPATH, "//*[@id='root']/main/section[1]/div/form/div/button")
        search_button.click()

    def get_ui_repo_count(self, username):
        self.open_user_page(username)
        time.sleep(5)
        repo_element = self.driver.find_element(By.XPATH, "//*[@id='root']/main/section[2]/section/article[1]/div/h3")
        repo_count_text = repo_element.text
        repo_count = int(repo_count_text.split()[0])
        return repo_count

    def get_ui_follower_count(self, username):
        self.open_user_page(username)
        time.sleep(5)
        followers_element = self.driver.find_element(By.XPATH,
                                                     "//*[@id='root']/main/section[2]/section/article[2]/div/h3")
        follower_count_text = followers_element.text
        follower_count = int(follower_count_text.split()[0])
        return follower_count

    def get_ui_following_count(self, username):
        self.open_user_page(username)
        time.sleep(5)
        following_element = self.driver.find_element(By.XPATH,
                                                     "//*[@id='root']/main/section[2]/section/article[3]/div/h3")
        following_count_text = following_element.text
        following_count = int(following_count_text.split()[0])
        return following_count

    def get_ui_gists_count(self, username):
        self.open_user_page(username)
        time.sleep(5)
        gists_element = self.driver.find_element(By.XPATH,
                                                 "//*[@id='root']/main/section[2]/section/article[4]/div/h3")
        gists_count_text = gists_element.text
        gists_count = int(gists_count_text.split()[0])
        return gists_count

    def get_ui_full_name(self, username):
        self.open_user_page(username)
        time.sleep(5)
        fullname_element = self.driver.find_element(By.XPATH,
                                                    "//*[@id='root']/main/section[3]/div/article[1]/header/div/h4")
        full_name = fullname_element.text
        return full_name

    def get_ui_twitter(self, username):
        self.open_user_page(username)
        time.sleep(5)
        twitter_element = self.driver.find_element(By.XPATH,
                                                   "//*[@id='root']/main/section[3]/div/article[1]/header/div/p")
        twitter = twitter_element.text
        return twitter

    def get_ui_bio(self, username):
        self.open_user_page(username)
        time.sleep(5)
        bio_element = self.driver.find_element(By.XPATH,
                                               "//*[@id='root']/main/section[3]/div/article[1]/p")
        bio = bio_element.text
        return bio

    def get_ui_company(self, username):
        self.open_user_page(username)
        time.sleep(5)
        company_element = self.driver.find_element(By.XPATH,
                                                   "//*[@id='root']/main/section[3]/div/article[1]/div/p[1]")
        company = company_element.text
        return company

    def get_ui_location(self, username):
        self.open_user_page(username)
        time.sleep(5)
        location_element = self.driver.find_element(By.XPATH,
                                                    "//*[@id='root']/main/section[3]/div/article[1]/div/p[2]")
        location = location_element.text
        return location

    def get_ui_blog(self, username):
        self.open_user_page(username)
        time.sleep(5)
        blog_element = self.driver.find_element(By.XPATH,
                                                "//*[@id='root']/main/section[3]/div/article[1]/div/a")
        blog = blog_element.text
        return blog

    def verify_blog_link(self, username):
        self.open_user_page(username)
        time.sleep(5)
        blog_element = self.driver.find_element(By.XPATH,
                                                "//*[@id='root']/main/section[3]/div/article[1]/div/a")
        blog_url = blog_element.get_attribute("href")
        if not blog_url:
            print(f"No blog link found for user {username}")
            return
        self.driver.execute_script(f"window.open('{blog_url}');")
        current_url = self.driver.current_url
        if current_url == blog_url:
            print(f"Blog link for user {username} redirects correctly to {blog_url}")
        else:
            print(f"Blog link for user {username} redirects to unexpected URL: {current_url}")

    def test_follow_button_redirect(self, username):
        self.open_user_page(username)
        time.sleep(5)
        follow_button = self.driver.find_element(By.XPATH, "//*[@id='root']/main/section[3]/div/article[1]/header/a")
        follow_button.click()
        time.sleep(5)
        current_url = self.driver.current_url
        expected_url = f"https://github.com/{username}"
        if current_url == expected_url:
            print(f"Follow link for user {username} redirects correctly to {expected_url}")
        else:
            print(f"Follow link for user {username} redirects to unexpected URL: {current_url}")

    def verify_follower_details(self, expected_login, expected_url):
        self.open_user_page("OlgaLesser")
        time.sleep(5)
        followers_list = self.driver.find_element(By.XPATH, "//*[@id='root']/main/section[3]/div/article[2]/div")
        followers = followers_list.find_elements(By.XPATH, "//*[@id='root']/main/section[3]/div/article[2]/div/article")
        for follower in followers:
            name_element = follower.find_element(By.XPATH, "//*[@id='root']/main/section[3]/div/article[2]/div/article/div/h4")
            link_element = follower.find_element(By.XPATH,
                                                 "//*[@id='root']/main/section[3]/div/article[2]/div/article/div/a")
            ui_name = name_element.text
            ui_url = link_element.get_attribute("href")
            if ui_name != expected_login:
                print(f"Mismatch: API follower name ({expected_login}) vs. Web UI ({ui_name})")
            else:
                print(f"Name matches: API and Web UI ({expected_login})")
            if ui_url != expected_url:
                print(f"Mismatch: API follower link ({expected_url}) vs. Web UI ({ui_url})")
            else:
                print(f"Link matches: API and Web UI ({expected_url})")
