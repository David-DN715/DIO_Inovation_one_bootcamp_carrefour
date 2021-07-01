import requests

#criamos abaixo uma função com a biblioteca request usando o metodo get() para abrir a uri
def consulta():
    response = requests.get('https://...')
    print(response.status_code)
    print(response.json())
    for pessoa in response.json():
        print(pessoa['id'], pessoa['nome'], pessoa['idade'])
        
#podemos inserir um nome!
def insere():
    nome = 'Joe'
    idade = 27
    pessoa = {'nome':nome, 'idade':idade}
    response = requests.post('https://...', json=pessoa)
    print(response.status_code)
    print(status.json())
    
    
consulta()

insere()
