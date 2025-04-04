#Act_1
# Declare una función denominada evens_and_odds . Toma un número entero 
# positivo como parámetro y cuenta el número de pares e impares en el 
# número.
def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"Pares: {evens}, Impares: {odds}"
print(evens_and_odds(100))

#Act_2
# Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número
def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(5))

#Act_3
# Llama a tu función is_empty, toma un parámetro y comprueba si está vacío o 
# no
def is_empty(item):
    if not item:
        return True
    return False
print(is_empty([]))
print(is_empty({}))
print(is_empty(''))
print(is_empty([1, 2, 3]))
print(is_empty('Hola'))

#Act_4
# Escribe diferentes funciones que toman listas. Deben calculate_mean, 
# calculate_median, calculate_mode, calculate_range, calculate_variance 
# calculate_std (desviación estándar).
from math import sqrt
from collections import Counter

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    frequency = Counter(numbers)
    mode = [key for key, value in frequency.items() if value == max(frequency.values())]
    return mode

def calculate_range(numbers):
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

def calculate_std(numbers):
    variance = calculate_variance(numbers)
    return sqrt(variance)
data = [1, 2, 3, 4, 5, 6, 6, 7, 8]
print(f"Media: {calculate_mean(data)}")
print(f"Mediana: {calculate_median(data)}")
print(f"Moda: {calculate_mode(data)}")
print(f"Rango: {calculate_range(data)}")
print(f"Varianza: {calculate_variance(data)}")
print(f"Desviación estándar: {calculate_std(data)}")
