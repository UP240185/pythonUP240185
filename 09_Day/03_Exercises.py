#Act_1
# Aquí tenemos un diccionario de personas. ¡Siéntete libre de modificarlo!

Persona = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


# * Comprobar si el diccionario de la persona tiene la clave habilidades, 
# si es así, imprimir la habilidad del medio en la lista de habilidades. 
if 'skills' in Persona:
    print("La skill de en medio es", Persona['skills'][len(Persona['skills'])//2])
else:
    print("No estan las skills en el diccionario")

# * Comprobar si el diccionario de la persona tiene la clave habilidades, 
# si es así, verificar si la persona tiene la habilidad 'Python' 
# e imprimir el resultado. 
if 'Python' in Persona['skills']:
    print("Python esta en las skills, mira", Persona['skills'])
else:
    print("No esta Python rey")

# * Si las habilidades de una persona solo tienen JavaScript y React, 
# imprimir('Él es un desarrollador front end'), si las habilidades 
# de la persona tienen Node, Python, MongoDB, imprimir('Él es un desarrollador 
# backend'), si las habilidades de la persona tienen React, Node y MongoDB, 
# imprimir('Él es un desarrollador fullstack'), de lo contrario imprimir
# ('título desconocido') - para resultados más precisos se pueden anidar más 
# condiciones! 
if 'JavaScript' in Persona['skills'] and 'React' in Persona['skills']:
    print("Es desarrollador front-end")
elif 'Node' in Persona['skills'] and 'Python' in Persona['skills'] and 'MongoDB' in Persona['skills']:
    print("Es desarrollador back-end")
elif 'React' in Persona['skills'] and 'Node' in Persona['skills'] and 'MongoDB' in Persona['skills']:
    print("Es desarrolador full-stack")
else:
    print("Titulo desconocido")

# * Si la persona está casada y vive en Finlandia, imprimir la información 
# en el siguiente formato:
if 'Finland' in Persona['country'] and Persona['is_marred'] is True:
    print("Asabeneh Yetayeh reside en Finlandia. Está casado.")





