#Act_1
# Declarar una lista vacía.
lista_vacía = list()
print(len(lista_vacía))

#Act_2
# Declarar una lista con más de 5 elementos.
jugadores_de_voley = ['Chema', 'Meño', 'Javi', 'Octavio', 'Polo', 'Brandon']
print("Los jugadores convocados para el juego son: ", jugadores_de_voley)

#Act_3
# Encuentra la longitud de tu lista.
print(len(jugadores_de_voley))

#Act_4
# Obtenga el primer elemento, el elemento del medio y el último 
# elemento de la lista.
jugador_central = jugadores_de_voley[3]

#Act_5
# Declara una lista llamada mixed_data_types, pon tu (nombre, 
# edad, altura, estado civil, dirección)
Nombre = 'Chema'
Edad = '19'
Altura = '185 m'
Estado_civil = 'Soltero'
Dirección = "Deliceto 103"
mixed_data_types = [Nombre, Edad, Altura, Estado_civil, Dirección]

#Act_6
# Declare una variable de lista denominada it_companies y asigne 
# valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle 
# y Amazon.
Compañías_TI = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Act_7
# Imprime la lista usando print().
print(Compañías_TI)

#Act_8
# Imprime el número de empresas en la lista.
print(len(Compañías_TI))

#Act_9
# Imprime la primera, la intermedia y la última empresa.
print(Compañías_TI[0])
print(Compañías_TI[3])
print(Compañías_TI[6])

#Act_10
# Imprima la lista después de modificar una de las empresas.
Compañías_TI_nuevas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon','Tesla']
print(Compañías_TI_nuevas)

#Act_11
# Agregar una empresa de TI a it_companies.
Compañías_TI_mas_nuevas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon','Tesla', 'Nvidia']

#Act_12
# Inserte una empresa de TI en el centro de la lista de empresas.
Compañías_TI_mas_que_nuevas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Intel' 'IBM', 'Oracle', 'Amazon','Tesla']

#Act_13
# Cambie uno de los nombres de la it_companies a mayúsculas 
# (¡excluido IBM!).
Compañías_TI_mas_que_nuevas_mayus = ['Facebook', 'Google', 'Microsoft', 'Apple', 'INTEL', 'IBM', 'Oracle', 'Amazon','Tesla']

#Act_14
# Une el it_companies con una cadena '#; '
res = '#; '.join(Compañías_TI_mas_que_nuevas_mayus)
print(res)

#Act_15
# Compruebe si existe una determinada empresa en la lista de 
# it_companies.
existencia = 'Microsoft' in Compañías_TI
print(existencia)

#Act_16
# Ordene la lista usando el método sort()
print(Compañías_TI_mas_que_nuevas_mayus.sort())

#Act_17
# Invierta la lista en orden descendente usando el método reverse()
print(Compañías_TI_mas_que_nuevas_mayus.reverse())

#Act_18
# Corta las 3 primeras empresas de la lista.
print(Compañías_TI_mas_que_nuevas_mayus[0:2])

#Act_19
# Corta las últimas 3 empresas de la lista.
print(Compañías_TI_mas_que_nuevas_mayus[6:8])

#Act_20
# Elimine la empresa o empresas de TI intermedias de la lista
print(Compañías_TI_mas_que_nuevas_mayus[3])

#Act_21
# Eliminar la primera empresa de TI de la lista
print(Compañías_TI_mas_que_nuevas_mayus[0])

#Act_22
# Eliminar la empresa o empresas de TI intermedias de la lista
print(Compañías_TI_mas_que_nuevas_mayus[3:5])

#Act_23
# Eliminar la última empresa de TI de la lista
print(Compañías_TI_mas_que_nuevas_mayus[8])

#Act_24
# Eliminar todas las empresas de TI de la lista
print(Compañías_TI_mas_que_nuevas_mayus[0:8])

#Act_25
# Destruye la lista de empresas de TI
del Compañías_TI_mas_que_nuevas_mayus

#Act_26
# Únete a las siguientes listas:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
unión = front_end + back_end
print(unión)

#Act_27
# Después de unirse a las listas de la pregunta 26. Copie la lista 
# unida y asígnela a una variable full_stack, luego inserte Python y 
# SQL después de Redux.
unión.insert(5, 'Python')
unión.insert(6, 'SQL')
print(unión)

print("Revisado")