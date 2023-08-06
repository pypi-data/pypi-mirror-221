import requests

class ScratchAPIClient:
    def __init__(self):
        print("It may take a while for ScratchForGetData to boot up like 3-10 seconds")
        self.base_url = "https://scratch-get-data.kokoiscool.repl.co"

    def get_follower_count(self, username, api_key):
        url = f"{self.base_url}/get/follower-count/{username}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the follower count as a string

    def is_scratcher(self, username, api_key):
        url = f"{self.base_url}/get/is_scratcher/{username}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip().lower() == "true"  # Return True or False based on the response

    def get_following_count(self, username, api_key):
        url = f"{self.base_url}/get/following-count/{username}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the following count as a string

    def get_wiwo(self, username, api_key):
        url = f"{self.base_url}/get/wiwo/{username}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the WiWo as a string

    def get_about_me(self, username, api_key):
        url = f"{self.base_url}/get/aboutme/{username}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the About Me text as a string

    def get_messages(self, username, api_key):
        url = f"{self.base_url}/get/messages/{username}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the Messages as a string

    def get_project_creator(self, project_id, api_key):
        url = f"{self.base_url}/get/project/creator/{project_id}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the project creator username as a string

    def get_project_name(self, project_id, api_key):
        url = f"{self.base_url}/get/project/name/{project_id}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the project name as a string

    def get_project_description(self, project_id, api_key):
        url = f"{self.base_url}/get/project/notes_and_credits/{project_id}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the project description as a string

    def get_project_instructions(self, project_id, api_key):
        url = f"{self.base_url}/get/project/instructions/{project_id}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the project instructions as a string

    def get_project_blocks(self, project_id, api_key):
        url = f"{self.base_url}/get/project/blocks/{project_id}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the project blocks as a string

    def get_forum_title(self, post_id, api_key):
        url = f"{self.base_url}/get/forum/title/{post_id}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the forum post title as a string

    def get_forum_category(self, post_id, api_key):
        url = f"{self.base_url}/get/forum/category/{post_id}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the forum post category as a string

    def get_scratch_user_country(self, username, api_key):
        url = f"{self.base_url}/get/user/country/{username}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the Scratch user's country as a string

    def get_studio_title(self, studio_id, api_key):
        url = f"{self.base_url}/get/studio/title/{studio_id}/"
        params = {
            "key": api_key
        }
        response = requests.get(url, params=params)
        return response.text.strip()  # Return the Scratch studio title as string

class TestConnection:

  def test():
    base_url = "https://scratch-get-data.kokoiscool.repl.co"
    
    url = f"{base_url}/ping/"

    response = requests.get(url)
    
    if response.status_code == 200:
      return 'ok'
    else:
      raise("ConnectionError")

