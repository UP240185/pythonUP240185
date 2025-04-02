#Act_1
# Crea un diccionario vacío llamado perro.
perro_dict = {}

#Act_2
# Agregue nombre, color, raza, patas, edad al diccionario de perros.
perro_dict['Nombre'] = 'Frida'
perro_dict['Color'] = 'Blanco y Cafe'
perro_dict['Raza'] = 'Chihuhua'
perro_dict['Patas'] = '4'
perro_dict['Edad'] = '2'

#Act_3
# Cree un diccionario de estudiante y agregue first_name, last_name, sexo, edad, 
# estado civil, habilidades, país, ciudad y dirección como claves para el 
# diccionario.
estudiante_dict = {
    'first_name':'Chema',
    'last_name':'Carrillo',
    'gender':'Masculino',
    'age':'18',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'México',
    'city':'Jalpa',
    'address':{
        'street':'J. Mota Padilla',
        'zipcode':'99603'
        }
}

#Act_4
# Obtener la longitud del diccionario del estudiante.
print(len(estudiante_dict))

#Act_5
# Obtenga el valor de las habilidades y verifique el tipo de datos, debe ser una 
# lista
print(estudiante_dict['skills'])
print(type(estudiante_dict['skills']))


#Act_6
# Modifique los valores de las habilidades agregando una o dos habilidades
estudiante_dict['skills'].append('Volleyball')
estudiante_dict['skills'].append('Si hago push 😉')
print(estudiante_dict)

#Act_7
# Obtener las claves del diccionario como una lista.
print(estudiante_dict.keys())

#Act_8
# Obtener los valores del diccionario como una lista.
print(estudiante_dict.values())

#Act_9
# Cambie el diccionario a una lista de tuplas usando el método items()
print(estudiante_dict.items())

#Act_10
# Eliminar uno de los elementos del diccionario.
estudiante_dict.popitem()
print(estudiante_dict)

#Act_11
# Eliminar uno de los diccionarios
del estudiante_dict['skills']
print(estudiante_dict)

