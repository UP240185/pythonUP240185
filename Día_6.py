#Level_1

#Act_1
# Crear una tupla vacía.
tupla_vacía = ()
tupla_vacía = tuple()

#Act_2
# Crea una tupla que contenga los nombres de tus hermanas y tus 
# hermanos (los hermanos imaginarios están bien).
tupla_niñas = ('Anita', 'Diana', 'Fer')
tupla_niños = ('Liam', 'Brandon', 'Meño')

#Act_3
# Unir tuplas de hermanos y hermanas y asignarlas a hermanos
tupla_hermanos = tupla_niñas + tupla_niños

#Act_4
# ¿Cuántos hermanos tienes?
print(len(tupla_hermanos))

#Act_5
# Modifique la tupla de hermanos y agregue el nombre de su 
# padre y madre y asígnelo a family_members
tupla_padres = ('Chema', 'Ana')
tupla_familia = tupla_hermanos + tupla_padres


#Level_2

#Act_1
# Desempaca a los hermanos y padres de family_members
tupla_familia[3:7]

#Act_2
# Crea tuplas de frutas, verduras y productos de origen animal. 
# Une las tres tuplas y asígnalas a una variable llamada 
# food_stuff_tp.
tupla_frutas = ('Sandia', 'Mango', 'Jicama')
tupla_verduras = ('Chila', 'Cebolla', 'Tomate')
tupla_animal_prod = ('Leche', 'Bisteck', 'Huevo')
food_stuff_tp = tupla_frutas + tupla_verduras + tupla_animal_prod

#Act_3
# Cambiar la tupla acerca de food_stuff_tp a una lista food_stuff_lt
food_stuff_lt = food_stuff_tp
print(food_stuff_lt)

#Act_4
# Corte el elemento o elementos del medio de la food_stuff_tp 
# tupla o lista de food_stuff_lt.
food_stuff_lt[3:5]

#Act_5
# Corta los tres primeros elementos y los tres últimos de 
# food_staff_lt lista
food_stuff_lt = food_stuff_lt[0:2] + food_stuff_lt[6:8]

#Act_6
# Eliminar la tupla food_staff_tp por completo
del food_stuff_lt

#Act_7
# Compruebe si un elemento existe en tupla:
# 1.- Comprobar si 'Estonia' es un país nórdico.
# 2.- Comprueba si 'Islandia' es un país nórdico.
países_nórdicos = ('Dinamarca', 'Finlandia','Islandia', 'Noruega', 'Suecia')
comprovacion_1 = 'Estonia' in países_nórdicos
print(comprovacion_1)
comprovacion_2 = 'Islandia' in países_nórdicos
print(comprovacion_2)
