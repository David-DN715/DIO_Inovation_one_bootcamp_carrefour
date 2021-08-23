import socket

#Passamoso .af_inetpara usar o ip
#passamos o sock_stream
#E usamos o sock_dgram para criaro data gram do usuario
#Criamosocliente UDP
s =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("CLIENTE SOCKET CRIADO COM SUCESSO!")

host = "Localhost"
porta = 5433
menssagem = "Olá servidor!\ntudona paz?\tquem diriaque eu iria consseguir fazer isso!"

try:
    #Imprimindocliente e menssagem
    print("Cliente" +menssagem)
    #usamos sendto() para enviar a menssagem fechada paraohost e
    # a porta abaixo que é a porta que o servidor estará ouvindo
    s.sendto(menssagem.encode(), (host, 5432))
    #aqui osdados e o servidor tem de enviar um arquivocomotamanho dentro do recvfrom()
    dados, servidor = s.recvfrom(4096)
    #aqui abrimos amenssagem do servidor
    dados = dados.decode()
    #e aquimostramos amenssagem
    print("Cliente"+dados)
finally:
    print("Cliente:Fechando a conexão!")
    #Fechamos a conexão!
    s.close()

