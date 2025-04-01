#Act_1
# Concatene la cadena 'Thirty', 'Days', 'Of', 'Python' 
# en una sola cadena, 'Thirty Days Of Python'.
palabra_1 = 'Thirty'
palabra_2 = 'Days'
palabra_3 = 'Of'
palabra_4 = 'Python'
espacio = ' '
frace_completa = palabra_1 + espacio + palabra_2 + espacio + palabra_3 + espacio + palabra_4
print(frace_completa)

#Act_2
# Concatene la cadena 'Coding', 'For' , 'All' en una sola cadena, 
# 'Coding For All'.
palabra_1 = 'Coding'
palabra_2 = 'For'
palabra_3 = 'All'
espacio = ' '
frace_completa = palabra_1 + espacio + palabra_2 + espacio + palabra_3
print(frace_completa)

#Act_3
# Declare una variable denominada company y 
# asígnela a un valor inicial "Coding For All".
company = 'Coding For All'

#Act_4
# Imprime la variable company usando print().
print(company)

#Act_5
# Imprima la longitud de la cadena de la empresa 
# utilizando el método len() y print().
print(len(company))

#Act_6
# Cambie todos los caracteres a letras mayúsculas 
# usando el método upper().
print(company.upper)

#Act_7
# Cambie todos los caracteres a letras minúsculas 
# usando el método lower().
print(company.lower)

#Act_8
# Utilice los métodos capitalize(), title(), swapcase() 
# para formatear el valor de la cadena Coding For All.
frace = 'Coding For All'
print(frace.capitalize())
print(frace.title())
print(frace.swapcase())

#Act_9
# Corta la primera palabra de la cadena Coding For All.
print(company[7:14])

#Act_10
# Compruebe si la cadena Codificación para todos 
# contiene una palabra Codificación 
# mediante el método index, find u otros métodos.
frace = 'Codificación para todos'
print(frace.find('Codificación'))

#Act_11
# Reemplace la palabra codificación en la cadena 
# 'Codificación para todos' a Python.
frace = 'Codificación para todos'
print(frace.replace('Codificación', 'codificación'))

#Act_12
# Cambie Python para todos a Python para todos mediante 
# el método replace u otros métodos.
frace = 'Python para todas'
print(frace.replace('Python para todas', 'Python para todos'))

#Act_13
# Divida la cadena 'Coding For All' 
# usando el espacio como separador (split()).
cadena = 'CodingForAll'
print(cadena.split(' '))

#Act_14
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
# dividió la cadena en la coma.
cadena = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(cadena.split(', '))

#Act_15
#¿Cuál es el carácter en el índice 0 en la cadena Codificación para todos?
print('El carácter en el índice 0 en la cadena Codificación para todos es: ', company[0])

#Act_16
# ¿Cuál es el último índice de la cadena Coding For All?
print("El último índice de la cadena 'Coding For All' es: ",company.rindex('l'))

#Act_17
# Qué carácter está en el índice 10 en la cadena 
# "Codificación para todos".
print("el índice 10 en la cadena 'Codificación para todos' es: ", company[10])

#Act_18
# Crea un acrónimo o una abreviatura para el nombre 'Python For Everyone'.
frace = 'Python For Everyone'
print("El acrónimo de 'Python For Everyone' es: ", frace[0] + frace[7] + frace[11])

#Act_19
#Cree un acrónimo o una abreviatura para el nombre 'Coding For All'.
frace = 'Universidad Politécnica de Aguascalientes'
print("El acrónimo para la face 'Universidad Politécnica de Aguascalientes' es: ", frace[0] + frace[12] + frace[27])

#Act_20
# Utilice index para determinar la posición 
# de la primera aparición de C en Coding For All.
frace = 'Coding For All'
print(frace.index('C'))

#Act_21
# Utilice el índice para determinar 
# la posición de la primera aparición de F en Codificación para todos.
frace = 'Coding For All'
print(frace.index('F'))

#Act_22
# Utilice rfind para determinar la posición 
# de la última aparición de l en Codificación para todas las personas.
frace = 'Coding For All'
print(frace.rfind('l'))

#Act_23
# Use index o find para encontrar la posició de la primera aparición 
# de la palabra 'porque' en la siguiente oración: 
# 'No se puede terminar una oración con porque porque porque porque 
# es una conjunción'
frace = 'No se puede terminar una oración con porque porque porque porque es una conjunción'
print(frace.find('porque'))

#Act_24
# Use rindex para encontrar la posición de la última aparición 
# de la palabra porque en la siguiente oración: 
# 'No puedes terminar una oración con porque porque 
# porque porque es una conjunción'.
frace = "No puedes terminar una oración con porque porque porque porque es una conjunción"
print(frace.rindex('porque'))

#Act_25
# Corta la frase "porque porque porque" en la siguiente oración: 
# "No puedes terminar una oración con porque porque porque porque 
# es una conjunción"
frace = 'No puedes terminar una oración con porque porque porque porque es una conjunción'
la_de_a_deveras = No_puedes_terminar_una_oración_con_porque_es_una_conjunción = frace[0:41] + frace[62:80]
print(la_de_a_deveras)

#Act_26
# Halla la posición de la primera aparición de la palabra 
# 'porque' en la siguiente oración: 
# 'No puedes terminar una oración 
# con porque porque porque porque es una conjunción'.
frace = 'No se puede terminar una oración con porque porque porque porque es una conjunción'
print(frace.find('porque'))

#Act_27
# Corta la frase "porque porque porque" en la siguiente oración: 
# "No puedes terminar una oración con porque porque porque porque 
# es una conjunción"
frace = 'No puedes terminar una oración con porque porque porque porque es una conjunción'
la_de_a_deveras = No_puedes_terminar_una_oración_con_porque_es_una_conjunción = frace[0:41] + frace[62:80]
print(la_de_a_deveras)

#Act_28
# ¿''Coding For All' comienza con una subcadena Coding?.
frace = 'Coding For All'
print("¿'Cogding For All' comienza con una subcadena Coding?", 'Coding' in "Cogding For All")

#Act_29
# ¿'Coding For All' termina con una codificación de subcadena?
frace = 'Coding For All'
print(cadena.endswith('All'))

#Act_30
# ' Codificación para todos', elimine los espacios finales izquierdo y derecho 
# en la cadena dada.
frace = ' Codificación para todos'
frade_chida = frace.strip(' ')

#Act_31
# ¿Cuál de las siguientes variables devuelve True cuando usamos el 
# método isidentifier():
# 30DaysOfPython
# thirty_days_of_python
frace_1 = '30DaysOfPython'
print(frace_1.isidentifier())
frace_2 = 'thirty_days_of_python'
print(frace_2.isidentifier())

#Act_32
# La siguiente lista contiene los nombres de algunas de las 
# bibliotecas de python: ['Django', 'Flask', 'Bottle', 'Pyramid', 
# 'Falcon']. Únase a la lista con un hash con cadena de espacio.
bibliotecas = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = ' '.join(bibliotecas)
print(resultado)

#Act_33
# Utilice la nueva secuencia de escape de línea para separar las 
# siguientes oraciones.
oración_1 = 'I am enjoying this challenge.'
oracion_2 = 'I just wonder what is next.'
print(oración_1.expandtabs('_'))
print(oracion_2.expandtabs('_'))

#Act_34
#Utilice una secuencia de escape de tabulación para escribir las 
# siguientes líneas.
print("Name\t\tAge\tCountry\t\tCity\nOctavio\t\t18\tMéxico\t\tAguascalientes")

#Act_35 
# Utilice el método de formato de cadena para mostrar lo siguiente:
radio = 10
area = 3.14 * radio ** 2
print('El área del circulo con radio {} son {} metros cuadrados.'.format(radio,area))

#Act_36 
# Realice lo siguiente utilizando métodos de formato de cadena:
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) #dos decimales depsues del punto
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

print("Revisado")