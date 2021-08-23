import random
import string

tamanho = 16
#Objeto chars recebe letras maisculas e minusculas pelometodo .ascii_letters
#e tambem caracteres especiasi especificados com as "" !
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+'
#rnd usa uma biblioteca do sistemachamadaos.urandom para usar characteres fornecidos pelo systema!
rnd = random.SystemRandom()
#Printamos segundo abaixo!
print("".join(rnd.choice(chars)for i in range(tamanho)))
