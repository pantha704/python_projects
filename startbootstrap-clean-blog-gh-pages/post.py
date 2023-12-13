import requests


class Post:
    def __init__(self):
        self.id = 0
        img_url_list = ['https://images.unsplash.com/photo-1533066636271-fdbe3e84ad80?ixlib=rb-4.0.3&ixid'
                        '=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2FjdHVzfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60',
                        'https://images.unsplash.com/photo-1606103920295-9a091573f160?ixlib=rb-4.0.3&ixid'
                        '=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Ym9yZWR8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60',
                        'https://plus.unsplash.com/premium_photo-1676232732001-34d904cd7544?ixlib=rb-4.0.3&ixid'
                        '=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZmFzdGluZ3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60']
        self.posts = requests.get("https://api.npoint.io/aa831263b7b9ed2bfe31").json()
        for i in range(0,len(self.posts)):
            self.posts[i]['img'] = img_url_list[i]

    def get_post(self, id):
        self.id = id
        post = self.posts[int(id)-1]
        return post