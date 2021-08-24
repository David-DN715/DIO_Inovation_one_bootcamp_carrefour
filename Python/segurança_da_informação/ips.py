#Biblioteacpara manipularmos ips
import ipaddress
#Criamos uma string com um ip qualquer
ip = '192.168.0.1'
#e aqui usamos a biblioteca ipaddress para formatar em ip a string!
endereco = ipaddress.ip_address(ip)
print(ip)
