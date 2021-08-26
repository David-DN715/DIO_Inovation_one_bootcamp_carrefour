import hashlib

texto = input("Digite o texto a ser gerado a hash:\n")
#UTF-8 = 8-bits unicode Transformation format,é oformato muito utilizado no mundo para representação de caracteres
resultado = hashlib.md5(texto.encode('UTF-8'))

print('O hash da string é: ', resultado.hexdigest())
