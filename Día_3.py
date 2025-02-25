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