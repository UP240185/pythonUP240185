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
