from datetime import date, time, datetime

def trabalhando_com_date():
    #usamos o date.today para acharmos a data de hoje!
    data_autal = date.today()
    #Usamos o strftime() e passamos como parametros %d que é o dia o %m que é o mes e %y que é o ano
    print(data_autal.strftime('%d/%m/%y'))

def trabalhando_com_time ():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))

def trabalhando_com_datetime():
    data_autal = datetime.now()
    print(data_autal)
    #pegando somene a data!
    print(data_autal.strftime('%d/%m/%y'))
    #pegando somente a hora
    print(data_autal.strftime('%H:%M:%S'))
    #Pegando um resulmo do que é geralmente usado/ um atalho!
    print(data_autal.strftime('%c'))
    #um exeplo muito bom!
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    #Trazemos em portugues o dia de hoje!
    print(tupla[data_autal.weekday()])

if __name__ == '__main__':
    trabalhando_com_datetime()
