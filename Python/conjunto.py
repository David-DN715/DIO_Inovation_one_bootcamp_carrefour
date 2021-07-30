conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
#Passamos a unir os dois conjuntos com a função de conjunto .union()
conjunto_uniao = conjunto.union(conjunto2)

#faremos a intersecção agora!
conjunto_intersec = conjunto.intersection(conjunto2)

#podemos chamar tambem a difeença!
conjunto_difenca = conjunto.difference(conjunto2)

---------------------------------------------------------------------------
#diferença simetrica!
# a diferença que existe nos dois conjuntos
conjunto_diff_simetric = conjunto.symmetric_difference(conjunto2)
print(conjunto_diff_simetric)
---------------------------------------------------------------------------
#Subset!
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
#verifica se os elementos que existe no conjunto a estão contido dentro de b!
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

#O superset() verifica se o conjunto b é um conjunto que contem mais elementos do que o conjunto a!
conjunto_superset = conjunto_b.issuperset(conjunto_a)
-----------------------------------------------------------------------------
lista = ['cachorro', 'papagaio', 'gato', 'morcego']
#assim se faz a conversão para conjunto!
conjunto_animais = set(lista)
