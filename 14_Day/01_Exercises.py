#Act_1 
# Explique la diferencia entre asignar, filtrar y reducir.

# 1.-Asignar (Map):
#   Se utiliza para transformar cada elemento de una lista (o iterable) aplicando una función. El resultado es una nueva lista con los elementos modificados.

# 2.-Filtrar (Filter):
#   Permite seleccionar elementos específicos de una lista (o iterable) que cumplen con una condición. El resultado es una lista más pequeña con los elementos que pasan el filtro.

# 3.-Reducir (Reduce):
# Reduce una lista (o iterable) a un único valor aplicando una función acumulativa. A menudo se utiliza para realizar operaciones como la suma, el producto o la concatenación.


#Act_2
# Explique la diferencia entre función de orden superior, cierre y decorador

# 1.-Función de Orden Superior (Higher-Order Function):
# Es una función que:
# * Toma una o más funciones como parámetros, o
# * Devuelve otra función como resultado.

# 2.-Cierre (Closure):
# Un cierre es una función que:
# * Recuerda las variables del entorno en el que fue definida, incluso después 
# de que ese entorno haya terminado su ejecución.

# 3.-Decorador (Decorator):
# Un decorador es una función de orden superior que:
# * Envuelve otra función para modificar o extender su comportamiento sin 
# cambiar su estructura original.


#Act_3
# Defina una función de llamada antes de asignar, filtrar o reducir, consulte ejemplos.
# Función de llamada: Duplicar un número
def double(x):
    return x * 2
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(double, numbers))
print(doubled_numbers)


#Act_4
# Utilice el bucle for para imprimir cada país en la lista de países.
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for country in countries:
    print(country)


#Act_5
# Utilícelo para imprimir cada nombre en la lista de nombres.
names = ['Asabeneh', 'David', 'Donald', 'Bill', 'Elon']
for name in names:
    print(name)


#Act_6
# Utilícelo para imprimir cada número de la lista de números.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)
print("Revisado")