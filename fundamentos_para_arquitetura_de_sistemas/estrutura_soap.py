# SOAP - Simple Object Acess Protocol
# SOAP - Protocolo de Simples Acesso ao Objeto

#SOAP Envelope – é o elemento principal do documento e os outros elementos ficam dentro dele.

#SOAP Header – é o elemento que possui atributos e metadados da requisição (IP, DNS, Credencias de autenticação, Token).

#SOAP Body – onde passamos os atributos os detalhes da mensagem. 

#O SOAP abaixo foi feito atraves do Framework soapUI, com um SOAP aberto (Publico! <http://www.soapclient.com/xml/soapresponder.wsdl>)
<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soap="http://www.SoapClient.com/xml/SoapResponder.xsd">
   <soapenv:Header/>
   <soapenv:Body>
      <soap:Method1 soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <bstrParam1 xsi:type="xsd:string">?</bstrParam1>
         <bstrParam2 xsi:type="xsd:string">?</bstrParam2>
      </soap:Method1>
   </soapenv:Body>
</soapenv:Envelope>
