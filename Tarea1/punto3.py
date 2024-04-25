### 1. Utiliza la biblioteca requests para obtener todos los usuarios (GET). ### 

import requests

# URL de la API JSONPlaceholder para obtener todos los usuarios
url = "https://jsonplaceholder.typicode.com/users"

# Realizar la solicitud GET
response = requests.get(url)

# Verificamos el estado de la respuesta
if response.status_code == 200:
    # La solicitud fue exitosa, muestra los datos de los usuarios
    users = response.json()
    print("Usuarios obtenidos exitosamente:")
    for user in users:
        print(user)
else:
    # La solicitud falló, muestra el código de estado
    print(f"Error al obtener usuarios. Código de estado: {response.status_code}")

### 2. Elige un usuario y actualiza su información (PUT o PATCH). ### 
# Elegimos un usuario y su ID para actualizar

user_id = 1  # por ejemplo

# Nueva información para el usuario
new_data = {
    "name": "Quinterito",
    "email": "carlos.quinterop@udea.edu.co",
    "phone": "3003524167"
}

# URL del usuario específico para actualizar
update_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

# Se envia la solicitud PATCH para actualizar la información
update_response = requests.patch(update_url, json=new_data)

# Verificamos el estado de la respuesta
if update_response.status_code == 200:
    print("Información del usuario actualizada exitosamente.")
else:
    print(f"Error al actualizar la información del usuario. Código de estado: {update_response.status_code}")

### 3. Crea un nuevo post para el usuario seleccionado (POST). ### 

# Datos del nuevo post
new_post_data = {
    "title": "Taller 1",
    "body": "Una tarea muy larga en clase de programación para la industria",
    "userId": user_id  # Utilizamos el ID del ejemplo anterior
}

# URL para crear un nuevo post
create_post_url = "https://jsonplaceholder.typicode.com/posts"

# Enviamos la solicitud POST para crear el nuevo post
create_post_response = requests.post(create_post_url, json=new_post_data)

# Verificamos el estado de la respuesta
if create_post_response.status_code == 201:
    print("Nuevo post creado exitosamente.")
else:
    print(f"Error al crear el nuevo post. Código de estado: {create_post_response.status_code}")

### 4. Elimina el post creado (DELETE). ### 

# Obtenemos el ID del post creado
post_id = create_post_response.json()["id"]

# URL del post específico para eliminar
delete_post_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

# Enviamos la solicitud DELETE para eliminar el post
delete_response = requests.delete(delete_post_url)

# Verificar el estado de la respuesta
if delete_response.status_code == 200:
    print("Post eliminado exitosamente.")
else:
    print(f"Error al eliminar el post. Código de estado: {delete_response.status_code}")
