#Level_2

# Ordene la lista y encuentre la edad mínima y máxima
# Agregue la edad mínima y la edad máxima nuevamente a la lista
# Encuentre la edad media (un elemento del medio o dos 
# elementos del medio divididos por dos)
# Encuentre la edad promedio (suma de todos los artículos 
# dividida por su número)
# Encuentre el rango de las edades (max menos min)
# Compare el valor de (min - promedio) y (max - promedio), use el 
# método abs()
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.insert(0, 19)
ages.insert(11, 26)
edad_media = int((ages[5] + ages[6])/2)
edad_promedio = sum(ages)/len(ages)
rango = ages[11] - ages[0]
comparacion = abs((ages[0]-edad_promedio) and (ages[11]-edad_promedio)) 
print("La edad media son",edad_media,"años.")
print("La edad promedio son",edad_promedio,"años.")
print("El rango de edades es de",rango,"años.")
print("La comparación es:",comparacion)

#Act_1
# Encuentre el (los) país (s) del medio en la lista de países.
import COUNTRIES as p
paises = p.countries
pais_middle = (len(paises))//2 #96
print("Los paises de en medio de la lista son",paises[95],"y",paises[96])

#Act_2
# Divida la lista de países en dos listas iguales si no es un país más 
# para la primera mitad.
first_list = paises[:96]
second_list = paises[96:]
print("Lista 1:",first_list)
print("Lista 2:",second_list)

#Act_3
# ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 
# 'Dinamarca']. Desempaqueta los tres primeros países y el resto 
# como países escandinavos.
p.countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
p1, p2, p3, * escandinavos = p.countries
print("Los paises escandinavos son", escandinavos)
