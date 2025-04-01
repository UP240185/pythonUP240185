#Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


#Act_1
# Unir A y B
AB = A.union(B)

#Act_2
# Buscar una intersección B 
intersecciión = A.intersection(B)

#Act_3
# Es un subconjunto de B
print(A.issubset(B))

#Act_4
# Son conjuntos disjuntos A y B.
A.isdisjoint(B)

#Act_5
# Unir A con B y B con A
AB = A.union(B)
BA = B.union(A)

#Act_6
# ¿Cuál es la diferencia simétrica entre A y B?
print(A.symmetric_difference(B))

#Act_7
# Eliminar los conjuntos por completo.
del AB
del BA

print("Revisado")