import requests


class Post:
    def __init__(self):
        self.id = 0
        self.response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        self.posts = self.response.json()

    def output(self, id=0):
        self.id = id
        if self.id == 0:
            return self.posts
        else:
            return self.posts[int(self.id) - 1]
