#Foi usado um arquivo de txt chammado hosts.txt!
#Importamos nossas bibliotecas que usaremos!
import os
import time
#abrios o arquivo .txt como arquivo!
with open('hosts.txt') as file:
    #colocamos a variavel dump para ler o file!
    dump = file.read()
    #atualizamos a variavel com o metodo splitlines()
    dump = dump.splitlines()
    #para cada ip em nosso arquivo:
    for ip in dump:
        print('Verificando o IP:', ip)
        print('-'*60)
        os.system('ping {}'.format(ip))
        time.sleep(5)
