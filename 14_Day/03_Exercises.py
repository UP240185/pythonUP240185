#Act_1
# Abra su shell interactivo de Python y pruebe todos los ejemplos que se tratan 
# en esta sección.

#1. Lista en mayúsculas utilizando map:
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola']
uppercase_countries = list(map(lambda country: country.upper(), countries))
print(uppercase_countries)

#2. Filtrar países con seis letras o más:
countries = ['Sweden', 'Norway', 'Denmark', 'Iceland']
six_or_more_letters = list(filter(lambda country: len(country) >= 6, countries))
print(six_or_more_letters)

#3. Usar reduce para sumar números:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)

#4. Concatenar cadenas de países usando reduce:
from functools import reduce
countries = ['Estonia', 'Finlandia', 'Suecia', 'Dinamarca', 'Noruega', 'Islandia']
sentence = reduce(lambda x, y: f"{x}, {y}", countries[:-1]) + f" y {countries[-1]} son países del norte de Europa"
print(sentence)

#5. Filtrar países que contienen una palabra clave:
countries = ['Finland', 'Iceland', 'Netherlands', 'Thailand']
contains_land = list(filter(lambda country: 'land' in country.lower(), countries))
print(contains_land)






















