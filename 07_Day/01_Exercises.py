#Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


#Act_1
# Encuentre la longitud del conjunto it_companies
len(it_companies)

#Act_2
# Añade 'Twitter' a it_companies
it_companies.add('Twitter')

#Act_3
# Inserte varias empresas de TI a la vez en el conjunto it_companies
it_companies.update(['Intel', 'Nvidia'])

#Act_3
# Eliminar una de las empresas del conjunto it_companies
it_companies.remove('Apple')
print(it_companies)

#Act_4
# ¿Cuál es la diferencia entre quitar y desechar?
'Quitar".remobe()": Es utilizado para eliminar un elemento específico.'
'Desechar ".discard()": elimina un elemento de un conjunto si existe, pero no genera un error si el elemento no está presente.'

print("Revisado")