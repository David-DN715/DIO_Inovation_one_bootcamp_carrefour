#Biblioteacpara manipularmos ips
import ipaddress
#Criamos uma string com um ip qualquer
ip = '192.168.0.100/24'
#e aqui usamos a biblioteca ipaddress para formatar em ip a string!
redes = ipaddress.ip_network(ip, strict=False)

for ip in redes:
    print(ip)
