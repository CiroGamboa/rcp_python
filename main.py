import clientInterface

user = ""
passw = ""

exit_program = False
state = -1

#see_posts = 1
#create_post = 2
#delete_post = 3

def login():
    # Login goes here
    inserted_user = input("\nIngrese su usuario\n")
    inserted_passw = input("\nIngrese contraseña\n")
    
    # Compare with DB
    global user
    global passw
    user = inserted_user
    passw = inserted_passw
    return True

def show_menu():
    print("\nChisme UPB\n Ingrese su acción")
    print("1. Ver posts")
    print("2. Crear post")
    print("3. Modificar post")
    print("4. Eliminar post")
    print("5. Salir")
    
    return input()


def create_post():
    post_data = {}
    post_name = input("Nombre del post:\n")
    post_data['name'] = post_name
    post_data['date'] = "today" # Aca se adquiriria la fecha actual
    post_data['updated'] = "today"
    post_data['author'] = user
    post_data['content'] = input("Contenido:\n")
    
    clientInterface.create_post(user, post_name, post_data)
    
def update_post():
    old_post_name = input("Ingrese el nombre del post a modificar:\n")
    new_post_name = input("Ingrese el nuevo nombre del post a modificar:\n")
    new_post_content = input("Ingrese el nuevo contenido del post a modificar:\n")
    clientInterface.delete_post(user, old_post_name)
    
    post_data = {}
    post_name = new_post_name
    post_data['name'] = post_name
    post_data['date'] = "today" # Aca se adquiriria la fecha actual
    post_data['updated'] = "today"
    post_data['author'] = user
    post_data['content'] = new_post_content
    
    clientInterface.create_post(user, post_name, post_data)
    

def delete_post():
    post_name = input("Ingrese el nombre del post a borrar:\n")
    clientInterface.delete_post(user, post_name)

while(not exit_program):
    
    if(state == -1):
        if(login()):
            state = 0
    
    elif(state == 0):
        state = int(show_menu())
        
    elif(state == 1):
        print(clientInterface.show_posts())
        state = 0
    
    elif(state == 2):
        create_post()
        state = 0
        
    elif(state == 3):
        update_post()
        state = 0
        
    elif(state == 4):
        delete_post()
        state = 0
    
    elif(state == 5):
        exit_program = True
    
    else:
        print("Pailas")
        state = 0
    