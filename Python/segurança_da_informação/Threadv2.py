#Importamos a biblioteca Thread
#Thread é uma parte do codigo que pode correr independente do progama principal
# esperando alguma ação para inicialo.
import time
from threading import Thread
import time
#Aqui deixamos somente uma função!
def carro(velocidade,piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {}\n'.format(piloto, trajeto))

#Fazemos a Thread das velocidades passando com argumentos dentro da Thread()
t_carro1 = Thread(target=carro, args=[1, 'Bruno'])
t_carro2 = Thread(target=carro, args=[2,  'Jubileu'])
#Iniciamos as Thread!
t_carro1.start()
t_carro2.start()
