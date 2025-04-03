#Act_1
# Itere de 0 a 10 usando el bucle for, haga lo mismo usando el bucle while.
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

#Act_2
# Iterar de 10 a 0 usando el bucle for, haga lo mismo usando el bucle while.
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

#Act_3
# Escribe un bucle que haga siete llamadas a print(), así obtenemos en la salida 
# el siguiente triángulo:
  #
  ##
  ###
  ####
  #####
  ######
  #######
for i in range(1, 8):
    print('*' * i)

#Act_4
# Utilice bucles anidados para crear lo siguiente:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(8):
    for j in range(7):
        print('#', end = ' ')
    print()

#Act_5
# Imprime el siguiente patrón:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range(11):
    print(f"{i} * {i} = {i * i}")

#Act_6
# Itere a través de la lista, ['Python', 'Numpy','Pandas','Django', 'Flask'] usando 
# un bucle for e imprima los elementos.
Lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for elementos in Lista:
    print(elementos)

#Act_7
# Use el bucle for para iterar de 0 a 100 e imprimir solo números pares.
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

#Act_8
# Use el bucle for para iterar de 0 a 100 e imprimir solo números impares
for i in range(101):
    if i % 2 != 0:
        print(i)
