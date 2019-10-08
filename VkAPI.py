import requests


class VkAPI:
    def __init__(self, name):
        self.api_url = 'https://api.vk.com/method/'
        self.user = name
        self.access_token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'

    def get_friend_list(self):
        response = requests.get(
            self.api_url + 'friends.get?user_id=' + str(self.user) + '&access_token=' + self.access_token + '&v=5.52')
        return response.json()

    def get_group_list(self, user_id=None):
        if user_id is None:
            user_id = self.user
        response = requests.get(
            self.api_url + 'groups.get?user_id=' + str(user_id) + '&access_token=' + self.access_token + '&v=5.52')
        return response.json()
