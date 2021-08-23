import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("SOCKET CRIADO COM SUCESSO!!!")

host ='localhost'
porta = 5432
#bind() liga o servidor com o cliente atravez do host e da porta
s.bind((host, porta))
menssagem = "\nSERVIDOR: Olá !\n quem diriané não!\tmas voce deu conta!"
#enquanto for verdade
while 1:
    dados,end = s.recvfrom(4096)

    if dados:
        print("Servidor enviando menssagem... ")
        s.sendto(dados + (menssagem.encode()), end)

