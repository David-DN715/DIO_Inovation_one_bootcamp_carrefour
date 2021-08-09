#O que estiver dentro do try vai ser tentado para tratar o erro
lista = [1, 10]
try:
    divisao = 10/1
    numero = lista[1]
    x=a
    #Tratamento do erropersonalisado!
except ZeroDivisionError:
    print("Não é possivel dividir por 0!")
except IndexError:
    print('Erro ao acessar um indice da lista!')
    #Coloco a msg de erro em uma variavel e exibo de um jeito personalizado
except BaseException as ex:
    print('erro desconhecido erro: {}'.format(ex))
