#Act_1
#Declara tu edad como variable entera
age = 18
print(age)
print(type(age))

#Act_2
#Declarar la altura como una variable flotante
h=8.0
print(h)
print(type(h))

#Act_3
# Declarar una variable que almacena un número complejo
numero_complejo = 3 + 4j

# Imprimir el número complejo
print(numero_complejo)

# Acceder a las partes real e imaginaria
print(f'Parte real: {numero_complejo.real}')
print(f'Parte imaginaria: {numero_complejo.imag}')

#Act_4
# Write a script that prompts the user to enter base an heigh
# of the traingle and calculate an area of this triangle
# (area = 0.5 * b * h).
b = float(input("Ingresa el valor base: "))
h = float(input("Ingresa el valor de la altura: "))
a = print("El area del trángulo es de: ", b*h/2)

#Act_5
# Escriba un script que pida al usuario que escriba el lado a,
# el lado b y el lado c del triángulo. Calcula el perímetro
# del triángulo (perímetro = a + b + c).
a = float(input("Ingresa el valor del lado a :"))
b = float(input("Ingrese el valor del lado b :"))
c = float(input("ingrese el valor del lado c :"))
p = print("El perimetro del triángulo es :", a+b+c)

#Act_6
# Obtenga la longitud y el ancho de un rectángulo mediante
# el mensaje. Calcula su área (área = largo x ancho)
# y perímetro (perímetro = 2 x (largo + ancho).
large = float(input("Ingresa el valor de lo largo del rectángulo :"))
width = float(input("Ingresa el valor de lo ancho del rectángulo :"))
a = print("El area del rectngulo es :", large*width)
p = print("El primetro del rectángulo es :", 2*(large*width))

#Act_7
# Obtenga el radio de un círculo usando el mensaje.
# Calcula el área (área = pi x r x r)
# y la circunferencia (c = 2 x pi x r) donde pi = 3.14.
pi = 3.14
r = float(input("Determina el valor del radio: "))
a = print("El area del círculo es: ", pi*r*r)
c = print("La circunferencia es :", 2*pi*r)

#Act_8
#Calcula la pendiente, la intersección con el eje x
# y la intersección con el eje y de y = 2x -2
m = 2
b = -2
x_intercept = -b / m
print("Pendiente (m): ", m)
print("Intersección en Y (b): ", b)
print("Intersección en X: ", x_intercept)

#Act_9
#La pendiente es (m = y2-y1/x2-x1).
# Halla la pendiente y la distancia euclidiana entre
# el punto (2, 2) y el punto (6,10).
x_1 = 2
y_1 = 2
x_2 = 6
y_2 = 10
import math
pendiente = ((y_2)-(y_1)/(x_2)-(x_1))
euclides = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
print("La pendiente es: ", pendiente)
print("La distancia euclidiana: ", euclides)

#Act_10
#Compara las pendientes de las tareas 8 y 9.
if pendiente:
    print("Las pendientes son iguales")
elif m > pendiente:
    print("La primer pendiente es mas grande")
else:
    print("La segunda pendiente es mas grande")

#Act_11
# Calcula el valor de y (y = x^2 + 6x + 9).
# Intenta usar diferentes valores de x
# y averigua en qué valor de x y va a ser 0.
x_valor = float(input("Ingresa un valor para x: "))
y_valor = (x_valor**2) + 6*x_valor + 9
print("De la ecuación y=(x**2) + 6*x + 9 para que sea", y_valor, "x tiene que ser", x_valor)

#Act_12
# Encuentra la longitud de 'pitón' y 'dragón'
# y haz una afirmación de comparación falsa.
print("¿La palabra pitón es mas larga que dragón?", len("pitón") < len("dragón"))

#Act_13
# Use el operador and para verificar si 'on'
# se encuentra tanto en 'python' como en 'dragon'
print("¿'on' se encuentra en piton y en dragon?", 'on' in "piton" and "dragon")

#Act_14
# Espero que este curso no esté lleno de jerga.
# Úselo en para verificar si hay jerga en la oración.
print("¿La frase 'Espero que este curso no esté lleno de jerga'?", 'jerga' in 'Espero que este curso no esté lleno de jerga')

#Act_15
# No hay 'encendido' tanto en el dragón como en la pitón.
print("¿hay la palabra'encendido' en draon como en 'piton'?", 'encender' in 'piton' and 'dragon')

#Act_16
# Encuentre la longitud del texto python 
# y convierta el valor en float y conviértalo en string.
print(str(float(len("pyton"))))

#Act_17
# Los números pares son divisibles por 2 y el resto es cero. 
# ¿Cómo se comprueba si un número es par o no usando python?
numero = int(float("Introduce un numero: "))
if numero % 2 == 0:
    print(numero, "El numero es par")
else:
    print(numero, "es igual a creo")

#Act_18
# Compruebe si la división del suelo de 7 por 3 
# es igual al valor int convertido de 2,7.
terreno = 7//3 == int(2.7)
print("¿la divición de 7 entre 3 es igual a 2.7?", terreno)

#Act_19
# Compruebe si el tipo '10' es igual al tipo 10.
ab = type('10') == type(10)
print("¿'10' es igual a 10?", ab)

# Act_20
# Comprueba si int('9.8') es igual a 10.
bc = int('8.9') == type(10)
print("¿'9.8' es igual a 10?", bc)

#Act_21
# Escriba un script que solicite al usuario
# que ingrese las horas y la tarifa por hora.
# ¿Calcular el pago de la persona?
horas = float(input("Introduce las horas trabajadas: "))
pago_por_hora = float(input("Introdyuce el pago por hora: "))
pago_total = horas * pago_por_hora
print("El pago total es de: ", pago_total)

#Act_22
# Escriba un script que solicite al usuario que introduzca 
# el número de años. Calcula el número de segundos 
# que una persona puede vivir. Supongamos que una persona 
# puede vivir cien años.
años = print(input("Introduce tu edad: "))
segundos = años * 365 * 24 * 60 * 60
print ("El total de segundos que ha vivido son: ", segundos)

#Act_23
# Escriba un script de Python que muestre la siguiente tabla.
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")