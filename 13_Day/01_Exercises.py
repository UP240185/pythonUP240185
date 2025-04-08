#Act_1
#Filtre solo el negativo y el cero en la lista mediante la comprensión de listas
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]

#Act_2
#Aplanar la siguiente lista de listas de listas a una lista unidimensional :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]

#Act_3
# Usando la comprensión de listas, cree la siguiente lista de tuplas:
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples_list)

#Act_4
# Aplanar la siguiente lista a una nueva lista:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]
print(flattened_countries)

#Act_5
# Cambie la siguiente lista por una lista de diccionarios:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_dicts = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(country_dicts)

#Act_6
# Cambie la siguiente lista de listas a una lista de cadenas concatenadas:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [" ".join(name) for sublist in names for name in sublist]
print(concatenated_names)

#Act_7
# Escriba una función lambda que pueda resolver una pendiente o una 
# intersección con el eje y de funciones lineales.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else "Pendiente indefinida"
print(slope(1, 2, 3, 6))
y_intercept = lambda m, x, y: y - m * x
print(y_intercept(2, 1, 2))


print("Revisado")





