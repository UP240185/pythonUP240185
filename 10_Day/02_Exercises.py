#Act_1
# Use el bucle for para iterar de 0 a 100 e imprimir la suma de todos los 
# números.
suma = 0
for i in range(101):
    suma += i
print("La suma de los números del 0 al 100 es:", suma)

#Act_2
# Use el bucle for para iterar de 0 a 100 e imprimir la suma de todos los pares y 
# la suma de todas las probabilidades.
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print("La suma de los números pares es:", suma_pares)
print("La suma de los números impares es:", suma_impares)
print("Revisado")