from xmlrpc.server import SimpleXMLRPCServer
from dbInterface import dbHandler
db = dbHandler()

def login():
    pass

def get_posts():
    return db.get_posts()

def create_post(user, post_name, post_data):
    return db.create_post(user, post_name, post_data)

def update_post():
    pass

def delete_post(user, post_name):
    return db.delete_post(user, post_name)


server = SimpleXMLRPCServer(("localhost", 8013), allow_none=True)
print("Listening on port 8000...")
#server.register_function(is_even, "is_even")
server.register_function(get_posts, "get_posts")
server.register_function(create_post, "create_post")
server.register_function(delete_post, "delete_post")
server.serve_forever()
