#Importamosopacote hashlib
import hashlib
#criamos 2 arquivos de texto iguais.
#Passamos estes arquivos para variaveis!
arquivo1 = 'texto.txt'
arquivo2 = 'texto2.txt'
#aqui usamos a hashlib comoparametro .new() para passar parametrosde encripitação!
hash1 = hashlib.new('ripemd160')
#aqui abrimos o arquivo e fazemos a atualização do hash1 e passamos o arquivo1 comoparametro
hash1.update(open(arquivo1, 'rb').read())
#O ripend160 é um algoritimo de encripitação de 160bits!
hash2 = hashlib.new('ripemd160')
#O rb dentro doopen é read binary!
hash2.update(open(arquivo2, 'rb').read())
#a função digest resume osdados passados pelo update()
if hash1.digest() != hash2.digest():
    print(f'O arquivo1 : {arquivo1} é diferente do arquivo2: {arquivo2}')
    #A função hexdigest() vai colocar em hexadecimal e trazer o nosso hash!
    print('O arquivo do texto.txt é : ',hash1.hexdigest())
    print('O arquivo de texto1.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo1:{arquivo1} é igual o arquivo2: {arquivo2}')
