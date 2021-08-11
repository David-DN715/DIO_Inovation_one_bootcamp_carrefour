import socket
import sys

def main():
    try:
        #dentro da biblioteca socket usaremos o metodo socket
        #usaremos o IP por isso socket.AF_INET
        #usamos o socket.SOCK_STREAM para usar o TCP
        #e passamos por utimo o protocolo TCP para protocolo!
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Connection fail!")
        print('ERRO: {}'.format(e))
        sys.exit()
    print("Socket criado com sucesso!")

    hostalvo= input("Digite o host alvo:\n")
    porta_alvo = input("Digite a porta a ser conectada:\n")

    try:
        s.connect((hostalvo, int(porta_alvo)))
        print(f"Cliente TCP conectado com sucesso no Host: {hostalvo} e na porta: {porta_alvo}")
        s.shutdown(2)
    except socket.error as e:
        print(f'Não foi possivel conectar no host: {hostalvo} e na porta: {porta_alvo}')
        print("Erro: {}".format(e))
        sys.exit()

if __name__ =="__main":
    main()
