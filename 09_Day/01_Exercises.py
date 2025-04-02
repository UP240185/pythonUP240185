#Act_1
# Obtener la entrada del usuario mediante input("Introduzca su edad: "). Si el 
# usuario tiene 18 años o más, dé su opinión: Tiene la edad suficiente para 
# conducir. Si es menor de 18 años, dé su opinión para esperar la cantidad de 
# años que faltan. 
Edad = input('Introdusca su edad: ')
if Edad > 18:
    print('Tiene la edad suficiente para conduci.')
else:
    print('Deve esperar la cantidad de años que faltan.')

#Act_2
# Compare los valores de my_age y your_age utilizando si ... más. ¿Quién es
# mayor (tú o yo)? Use input("Ingrese su edad: ") para obtener la edad como 
# entrada. Puede usar una condición anidada para imprimir "año" para 1 año de 
# diferencia de edad, "años" para diferencias mayores y un texto personalizado si
# my_age = your_age. 
Mi_Edad = 18
Tu_Edad = int(input('Introduce tu edad: '))
Dieferiencia = Tu_Edad - 18
if Mi_Edad == Tu_Edad:
    print('Tenemos la misma edad')
elif Mi_Edad > Tu_Edad:
    print('Soy mas mayor que tu')
else:
    print('tenemos',Dieferiencia,'años de diferiencia')

#Act_3
# Obtenga dos números del usuario mediante la solicitud de entrada. Si a es 
# mayor que b, devuelve a es mayor que b, si a es menor, b devuelve a es menor 
# que b, de lo contrario, a es igual a b.
a = int(input('Introduce un número: '))
b = int(input('Introduce otro número: '))
if a > b:
    print('a es mas grande que b')
elif a < b:
    print('b es mas grande que a')
else:
    print('a y b son iguales')
