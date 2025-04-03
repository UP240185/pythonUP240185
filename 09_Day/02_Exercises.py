#Act_1
# Escriba un código que califique a los estudiantes de acuerdo con sus 
# puntuaciones:
Nota = int(input('Introduce la nota del examen: '))
if Nota <= 100 and Nota >= 90:
    print('Tu nota es "A"')
elif Nota <= 89 and Nota >= 70:
    print('Tu nota es "B"')
elif Nota <= 69 and Nota >= 60:
    print('Tu nota es "C"')
elif Nota <= 59 and Nota >= 50:
    print('Tu nota es "D"')
elif Nota <= 49 and Nota >= 0:
    print('Tu nota es "F"')

#Act_2
# Comprueba si la temporada es Otoño, Invierno, Primavera o Verano. Si la 
# entrada del usuario es: Septiembre, octubre o noviembre, la estación es el 
# otoño. Diciembre, enero o febrero, la temporada es invierno. Marzo, abril o 
# mayo, la estación es la primavera Junio, julio o agosto, la temporada es verano
Mes = str(input('Introduce el mes actual: '))
if Mes == 'Marzo' or Mes == 'Abril' or Mes == 'Mayo':
    print('La temporada es Primavera')
elif Mes == 'Junio' or Mes == 'Julio' or Mes == 'Agosto':
    print('La temporada es Verano')
elif Mes == 'Septiembre' or Mes == 'Octubre' or Mes == 'Noviembre':
    print('La temporada es Otoño')
elif Mes == 'Diciembre' or Mes == 'Enero' or Mes == 'Febrero':
    print('La tempoorada es Invierno')

#Act_3
# Si una fruta no existe en la lista, agregue la fruta a la lista 
# e imprima la lista modificada. Si la fruta existe, 
# imprima('Esa fruta ya existe en la lista')
Frutas = ['Platano', 'Naranja', 'Mango', 'limón']
Fruta = str(input('Introduce el nombre de alguna fruta: '))
if Fruta == 'Platano' or Fruta == 'Naranja' or Fruta == 'Mango' or Fruta == 'Limón':
    print('Esa fruta ya está en la lista')
else:
    Frutas.append(Fruta)
print(Frutas)