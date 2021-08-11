#Importamos o Os e integramos com o Os
import os
#printamos 60 vezes o '-'
print('-'*60)
#variavel armazena a informação de ip ou host!
ip_host = input('Digite o IP ou Host a verificar:\n')
#Usamos o metodo do Os.system para enviar 6 pacotes para ter de resposta o ping!
#-n é o numero de pacotes do sistemas a enviar que serão 6
os.system('ping -n 6 {}'.format(ip_host))
