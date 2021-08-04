#A funcao abaixo conta letras dentro de uma variavel!
def cont_let(lista):
    contador = []
    for x in lista:
        quantidade = len(x)
        contador.append(quantidade)
    return contador
#Lambda!
contador_letras = lambda lista : [len(x) for x in lista]

lista_animais = ['cachorro', 'vaca', 'cavalo']

print(contador_letras(lista_animais))
