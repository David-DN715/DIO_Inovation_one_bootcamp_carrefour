import hashlib

#definição do menu que usamos para o Ux!(User experience)
def menu():
    print('-----MENU-----')
    print('-----SOMENTE O NUMERO DA OPÇÃO!!!-----')
    print('1- MD5')
    print('2- SHA1')
    print('3- SHA256')
    print('4- SHA512')
    print('0- SAIR')

#Função abaixo recebe um texto para converter em md5!
def md5(texto):
    texto = hashlib.md5(texto.encode('UTF-8'))
    return print('O hash MD5 do texto é: ', texto.hexdigest())

#Função recebe texto para converter em sha1!
def sha1(texto):
    texto = hashlib.sha1(texto.encode('UTF-8'))
    return print(f'O sha1 do texto é: {texto.hexdigest()}')

#Função abaixo recebe textopara converter em sha256
def sha256(texto):
    texto = hashlib.sha256(texto.encode('UTF-8'))
    return print(f'O Sha256 do texto é: {texto.hexdigest()}')

#Função abaixo recebe texto para converter em sha512
def sha512(texto):
    texto = hashlib.sha512(texto.encode('UTF-8'))
    return print(f'O sha512 do texto é: {texto.hexdigest()}')

#Aqui começão nosso codigo principal!
verdade = True
while verdade:
    menu()
    opcao = int(input('Digite a opção:\n'))
    if opcao ==1:
        texto = input("Digite o texto a ser gerado a hash:\n")
        md5(texto)
    elif opcao==2:
        texto = input("Digite o texto a ser gerado a hash:\n")
        sha1(texto)
    elif opcao==3:
        texto = input("Digite o texto a ser gerado a hash:\n")
        sha256(texto)
    elif opcao ==4:
        texto = input("Digite o texto a ser gerado a hash:\n")
        sha512(texto)
    elif opcao == 0:
        verdade =False
        print('Thanks for your visit!!!!')
    else:
        menu()
        opcao = int(input('Digite a opção:\n'))
