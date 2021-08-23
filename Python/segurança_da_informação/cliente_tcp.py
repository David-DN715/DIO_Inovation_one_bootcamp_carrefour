import socket
import sys

def main():
    #passamoso af_inet onde utliza do ip
    #3soc_stream onde usamos o tcp
    #passamoso protocolo que fara a conexão com o server 0
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Conexão falhou!")
        print("ERRO: {}".format(e))
        sys.exit()

    print("CONEXÃO SOCKET CRIADOCOM SUCESSO!")
    hostalvo = input("Digite umhost ou ip a ser conectado:\n")
    portalvo = input("Digite a porta a ser conectada:\n")

    try:
        s.connect((hostalvo,int(portalvo)))
        print("Clientetcp conectadocom sucesso! no host:" +hostalvo,"na porta:" +portalvo)
        s.shutdown(2)

    except socket.error as e:
        print("A conexão falhou!")
        print("ERRO {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()
