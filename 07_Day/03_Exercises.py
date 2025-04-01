#Level 3
Lista_edades = [22, 19, 24, 25, 26, 24, 25, 24]


#Act_1
# Convierte las edades en un conjunto y compara la longitud de la 
# lista y el conjunto, ¿cuál es más grande?
Conjunto_edades = set(Lista_edades)

#Act_2
# Explique la diferencia entre los siguientes tipos de datos: cadena, 
# lista, tupla y conjunto.
'Cadena (String)'
'Es una secuencia de caracteres, como texto, que está delimitada por comillas simples o dobles'

'Lista (list)'
'Es una colección ordenada de elementos que puede contener distintos tipos de datos (números, cadenas, etc.).'

'Tupla (tuple)'
'Similar a una lista, es una colección ordenada de elementos, pero inmutable: no puedes modificar sus elementos después de creada.'
'Se define usando paréntesis ().'

'Conjunto (set)'
'Es una colección desordenada y única, lo que significa que no permite elementos duplicados.'
'Se define usando llaves {}.'

#Act_3
# Soy profesora y me encanta inspirar y enseñar a la gente. 
# ¿Cuántas palabras únicas se han utilizado en la oración? Utilice 
# los métodos de división y conjunto para obtener las palabras 
# únicas.
oracion = 'Soy profesora y me encanta inspirar y enseñar a la gente'
palabras = oracion.split()
palabras_unicas = set(palabras)
print(len(palabras_unicas))


print("Revisado")