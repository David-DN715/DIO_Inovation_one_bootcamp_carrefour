#Instalamos o pacote caso não tenha em seu ecosistema python!
!pip install -q zeep

#importamos a biblioteca!
from zeep import Client

#Abrimos o Client com uma URI na qual pertence o SOAP!
client = Client('http://www.soapclient.com/xml/soapresponder.wsdl')
#chamamos de cliente dentro do metodo Method1 e passamos os parametros!
result = client.service.Method1(bstrParam1 = 'oi', bstrParam2 = 'Tchal !')
#exibimos o resultado!
print(result)
