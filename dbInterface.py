import pickle

class dbHandler:
    def __init__(self):
        self.db = {}

        try:
            with open('db_rpc', 'rb') as f:
                self.db = pickle.load(f)
        
        except:
            test_name = "testuser"
            test_user = {
                        "user": test_name,
                        "passw": "123",
                        "rol": "user"
                        "posts": {
                            "testpost": {
                                "name": "testpost",
                                "date": "today",
                                "updated": "today",
                                "author": test_name,
                                "content": "cositas test"
                                    
                                    }
                                }
                        }
                            
                            
            self.db[test_name] = test_user
            
            test_admin_name = "testadmin"
            test_admin = {
                            "user": test_admin_name,
                            "passw": "567",
                            "rol": "admin",
                            "posts": {}
                    }
            
            self.db[test_admin_name] = test_admin
        #print(self.db)

    def get_posts(self):
        posts = []
        for user in self.db:
            for post in self.db[user]["posts"]:
                #print(user["posts"])
                posts.append(self.db[user]["posts"][post])
                #print(post)
        
        #print(posts)
        return posts
                
            
    
    def create_post(self, user, post_name, post_data):
        self.db[user]["posts"][post_name] = post_data
    
    def update_post():
        pass
    
    def delete_post(self, user, post_name):
        self.db[user]["posts"].pop(post_name)
    
    
################## tests
'''       
db = dbHandler()
db.get_posts()


user = "testuser"
post_name = "segundo post"
post_data = {'name': 'segundo post', 'date': 'today', 'updated': 'today', 'author': 'testuser', 'content': '2222222'}

db.create_post(user, post_name, post_data)
db.get_posts()
'''