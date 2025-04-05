#Act_1
# Escribe una función que genera un random_user_id de seis dígitos/caracteres.
import random
import string
def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(6))
    return random_id
user_id = generate_random_user_id()
print("Random User ID:", user_id)

#Act_2
# Modifique la tarea anterior. Declare una función denominada 
# user_id_gen_by_user. No toma ningún parámetro, pero toma dos entradas 
# usando input(). Una de las entradas es el número de caracteres y la segunda 
# entrada es el número de ID que se supone que se van a generar.
import random
import string
def user_id_gen_by_user():
    num_characters = int(input("Introduce el número de caracteres por ID: "))
    num_ids = int(input("Introduce el número de IDs a generar: "))
    for _ in range(num_ids):
        characters = string.ascii_letters + string.digits
        random_id = ''.join(random.choice(characters) for _ in range(num_characters))
        print("Random User ID:", random_id)
user_id_gen_by_user()

#Act_3
# Escriba una función denominada rgb_color_gen. Generará colores rgb (3 
# valores que van de 0 a 255 cada uno).
import random
def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)
color_rgb = rgb_color_gen()
print("Color RGB generado:", color_rgb)
