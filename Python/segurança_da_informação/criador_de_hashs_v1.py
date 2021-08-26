import hashlib
#o b na frente do aopstofo dentro do md5() é usadopara converter a string em byts
resultado = hashlib.md5(b'Phyton security')

print('O hash da string é: ', resultado.hexdigest())
