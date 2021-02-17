import xmlrpc.client

#with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
#    print("3 is even: %s" % str(proxy.is_even(3)))
#    print("100 is even: %s" % str(proxy.is_even(100)))

server_addr = "http://localhost:8013/"

def show_posts():
    print("\nMostrando Posts")
    with xmlrpc.client.ServerProxy(server_addr,allow_none=True) as proxy:
        return proxy.get_posts()
    
def create_post(user, post_name, post_data):
    with xmlrpc.client.ServerProxy(server_addr,allow_none=True) as proxy:
        return proxy.create_post(user, post_name, post_data)

def update_post(user, post_name):
    pass


def delete_post(user, post_name):
    with xmlrpc.client.ServerProxy(server_addr,allow_none=True) as proxy:
        return proxy.delete_post(user, post_name)
    