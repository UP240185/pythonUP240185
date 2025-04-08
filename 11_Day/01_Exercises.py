#Act_1
# Declarar una función add_two_numbers. Toma dos parámetros y devuelve una 
# suma.
def add_two_numbers(a, b):
    return a + b
resultado = add_two_numbers(3, 5)
print("La suma es:", resultado)

#Act_2
#El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escriba 
# una función que calcule area_of_circle.
import math
def area_circulo(radius):
    return math.pi * radius * radius
radio = 5
area = area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area:.2f}")

#Act_3
# Escriba una función llamada add_all_nums que tome un número arbitrario de 
# argumentos y sume todos los argumentos. Compruebe si todos los elementos 
# de la lista son tipos de números. Si no es así, dé una retroalimentación 
# razonable.
def add_all_nums(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "Error: Todos los argumentos deben ser números (int o float)."
resultado = add_all_nums(1, 2, 3.5, 4)
print("Resultado:", resultado)
resultado_incorrecto = add_all_nums(1, 2, "tres", 4)
print("Resultado:", resultado_incorrecto)

#Act_4
# La temperatura en °C se puede convertir a °F usando esta fórmula: 
# °F = (°C x 9/5) + 32. Escribe una función que convierta °C a °F, 
# convert_celsius_to-fahrenheit.
def convertir_celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius_temp = 25
fahrenheit_temp = convertir_celsius_a_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C es igual a {fahrenheit_temp}°F")

#Act_5
# Escriba una función llamada check-season, toma un parámetro de mes y 
# devuelve la temporada: Otoño, Invierno, Primavera o Verano.
def check_season(Mes):
    Mes = Mes.lower()
    if Mes in ['diciembre', 'enero', 'febrero']:
        return "Invierno"
    elif Mes in ['marzo', 'abril', 'mayo']:
        return "Primavera"
    elif Mes in ['junio', 'julio', 'agosto']:
        return "Verano"
    elif Mes in ['septiembre', 'octubre', 'noviembre']:
        return "Otoño"
    else:
        return "Mes no válido. Por favor ingrese un mes válido."
Mes = "Abril"
temporada = check_season(Mes)
print(f"{Mes} pertenece a la temporada: {temporada}")

#Act_6
# Escribe una función llamada calculate_slope que devuelva la pendiente de una 
# ecuación lineal
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "La pendiente es indefinida (división por cero)."
    slope = (y2 - y1) / (x2 - x1)
    return slope
x1, y1 = 3, 2
x2, y2 = 7, 6
pendiente = calculate_slope(x1, y1, x2, y2)
print(f"La pendiente entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {pendiente}")

#Act_7
# La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. 
# Escribe una función que calcule el conjunto de soluciones de una ecuación 
# cuadrática, solve_quadratic_eqn.
import math
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "No es una ecuación cuadrática (a no puede ser 0)."
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return "No hay soluciones reales (discriminante negativo)."
a, b, c = 1, -3, 2
soluciones = solve_quadratic_eqn(a, b, c)
print(f"Las soluciones de la ecuación son: {soluciones}")

#Act_8
# Declare una función denominada print_list. Toma una lista como parámetro e 
# imprime cada elemento de la lista.
def print_list(elements):
    for element in elements:
        print(element)
my_list = [1, "hola", True, 3.14]
print_list(my_list)

#Act_9
# Declare una función denominada reverse_list. Toma una matriz como 
# parámetro y devuelve lo contrario de la matriz (bucles use).
def reverse_list(elements):
    reversed_list = []
    for i in range(len(elements) - 1, -1, -1):
        reversed_list.append(elements[i])
    return reversed_list
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

#Act_10
# Declare una función denominada capitalize_list_items. Toma una lista como 
# parámetro y devuelve una lista de elementos en mayúsculas
def capitalize_list_items(items):
    capitalized_items = []
    for item in items:
        capitalized_items.append(item.upper())
    return capitalized_items
my_list = ["python", "programación", "aprendizaje"]
capitalized_list = capitalize_list_items(my_list)
print(f"Lista original: {my_list}")
print(f"Lista en mayúsculas: {capitalized_list}")

#Act_11
# Declare una función denominada add_item. Toma una lista y un elemento 
# parámetros. Devuelve una lista con el elemento agregado al final.
def add_item(items, item):
    items.append(item)
    return items
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

#Act_12
# Declare una función denominada remove_item. Toma una lista y un elemento 
# parámetros. Devuelve una lista con el elemento eliminado de ella.
def remove_item(items, item):
    if item in items:
        items.remove(item)
    return items
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#Act_13
# Declare una función denominada sum_of_numbers. Toma un parámetro 
# numérico y suma todos los números de ese rango.
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Act_14
# Declare una función denominada sum_of_odds. Toma un parámetro numérico 
# y suma todos los números impares en ese rango.
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total
print(sum_of_odds(5)) 
print(sum_of_odds(10))
print(sum_of_odds(100))

#Act_15
# Declare una función denominada sum_of_even. Toma un parámetro numérico 
# y suma todos los números pares en ese rango.
def sum_of_even(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_even(5))
print(sum_of_even(10))
print(sum_of_even(100))
print("Revisado")