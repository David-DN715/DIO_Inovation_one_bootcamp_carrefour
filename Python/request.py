import requests

def retorna_dados_pokemon (pokemon):
    response = requests.get(f'https://Apipokemon{pokemon}/')
    dados_pokemon = response.json()
    return dados_pokemon

if __name__ == '__main__':
    pokemon = input('digite o nome de um pokemon:\n')
    print(retorna_dados_pokemon(pokemon))
