#Act_1
#Llame a su función shuffle_list, toma una lista como parámetro y devuelve una 
# lista mezclada
import random
def shuffle_list(input_list):
    shuffled = input_list.copy()
    random.shuffle(shuffled)
    return shuffled
original_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(original_list)
print("Lista original:", original_list)
print("Lista mezclada:", shuffled_list)

#Act_2
# Escriba una función que devuelva una matriz de siete números aleatorios en 
# un rango de 0 a 9. Todos los números deben ser únicos.
import random
def unique_random_numbers():
    return random.sample(range(10), 7)
unique_numbers = unique_random_numbers()
print("Números únicos generados:", unique_numbers)
print("Revisado")