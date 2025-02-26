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

#Act_8, 9 y 10
# Calcula la pendiente, la intersección con el eje x
# y la intersección con el eje y de y = 2x -2
import math

# Ecuación de la línea y = 2x - 2
m_eq = 2  # Pendiente
b_eq = -2  # Intersección con el eje y

# Intersección con el eje y
interseccion_y = b_eq

# Intersección con el eje x
interseccion_x = -b_eq / m_eq

print(f'Pendiente de la ecuación y = 2x - 2: {m_eq}')
print(f'Intersección con el eje y: (0, {interseccion_y})')
print(f'Intersección con el eje x: ({interseccion_x}, 0)')

# Puntos
x1, y1 = 2, 2
x2, y2 = 6, 10

# Cálculo de la pendiente entre los puntos
m_puntos = (y2 - y1) / (x2 - x1)

# Cálculo de la distancia euclidiana
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'Pendiente entre los puntos ({x1}, {y1}) y ({x2}, {y2}): {m_puntos}')
print(f'Distancia euclidiana entre los puntos: {d}')

# Comparación de pendientes
print(f'¿Las pendientes son iguales? {"Sí" if m_eq == m_puntos else "No"}')

#Act_11
#Calcula el valor de y (y = x^2 + 6x + 9).
# Intenta usar diferentes valores de x
# y averigua en qué valor de x y va a ser 0.
import numpy as np

# Definir la función
def calcular_y(x):
    return x**2 + 6*x + 9

# Probar diferentes valores de x
valores_x = np.array([-10, -5, 0, 2, 3, 5, 10])
valores_y = calcular_y(valores_x)

# Encontrar el valor de x donde y es 0
x_cero = -3  # Dado que (x + 3)^2 = 0 cuando x = -3

print("Valores de y para diferentes valores de x:")
for x, y in zip(valores_x, valores_y):
    print(f"x = {x}, y = {y}")

print(f"\nEl valor de x para el cual y = 0 es: x = {x_cero}")

#Act_12
#Encuentra la longitud de 'pitón' y 'dragón'
# y haz una afirmación de comparación falsa.
piton = 5
dragon = 6
print("La longitud de 'pitón' es: ", 5)
print("La longitud de 'dragón' es: ",  6)
print("Es falso que la longitud de 'pitón' sea mayor que la de 'dragón' porque 5 no es mayor que 6.")

#Act_13
# Palabras
palabra1 = "python"
palabra2 = "dragon"

# Verificar si 'on' está en ambas palabras
resultado = ('on' in palabra1) and ('on' in palabra2)

print(f"¿'on' se encuentra tanto en 'python' como en 'dragon'? {resultado}")

#Act_14
