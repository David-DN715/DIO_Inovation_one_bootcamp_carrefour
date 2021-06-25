#importando todos os pacotes que serão nescessario para nosso projeto de machine learning!
import pandas as pd
import numpy as np
#dois pacotes que não havia usado ainda, aprender é tudo!
#suporte a arvores de decisao, e objeto para decisao!
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#faremos a leitura dos dados!
dados = pd.read_csv('train.csv')

#Encabeçamos os dados!
dados.head()

#Eliminamos com a função drop() algumas informaçoes que não vamos precisar!
dados = dados.drop(['Name', 'Ticket', 'Embarked', 'Cabin'], axis = 1)

#Representamos de novamente o head mais limpo!
dados.head()

#aqui retiramos a contagem da linha, somente passagemId!
dados.set_index(['PassengerId'])

#e agora damos como alvo os sobreviventes e renomeamos para Target!
dados = dados.rename(columns = {'Survived' : 'Target'} , inplace = False)
#e agora damos como alvo os sobreviventes e renomeamos para Target!
dados = dados.rename(columns = {'Survived' : 'Target'} , inplace = False)

#passamos um geral por toda a tabela ao inves de só o cabeçalho!
dados.describe()

#passamos aqui a descrição pois tinhamos homens e mulheres no navio Titanic!
dados.describe(include=['O'])

#transformamos dados!
#usamos um dos metodos em numpy where() para mudarmos elementos dentro do nosso dado
dados['Sex_F'] = np.where(dados['Sex'] == 'female', 1, 0)

#Nos mudamos os dados abaixo pois muitos modelos de machine learning não aceita dados categoricos como o exemplo de sexo
#masculo ou feminino!
#por isso no exemplo abaixo trocamos o feminino por 1 e masculino por 0!
#lembrando que machine learning usa algoritimos matematicos e strings dificultam a sua execuçao!
dados['Class_1'] = np.where(dados['Pclass']== 1, 1, 0)
dados['Class_2'] = np.where(dados['Pclass']== 2, 1, 0)
dados['Class_3'] = np.where(dados['Pclass']== 3, 1, 0)

#aqui usamos a função drop para 
dados = dados.drop(['Pclass', 'Sex'], axis = 1)

dados.head()

#Com o comando abaixo verificamos se os dados missing são realmente só em um unico dados!
dados.isnull().sum()

#substituimos os valores mssing na idade por 0
dados.fillna(0, inplace = True)

dados.isnull().sum()

#Aqui temos nosso modelo de amostragem!
#esse modelo é para verificar a precisão dos dados, splitandos em 2 pedaços para verificar o quao bom é o modelo!
#Fonte: https://www.tutorialspoint.com/scikit_learn/scikit_learn_modelling_process.htm
#Splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(dados.drop(['Target'], axis =1)\
                                                    ,dados['Target'], test_size = 0.3, random_state = 1234)
[{'Treino' : x_train.shape} , {'Teste': x_test.shape}]

#aqui nos usamos o metodo dentro do skit learn para florestas randomicas!
#pedimos para ser gerado 1000 arvore diferentes usando o criterio gini e tenha no maximo de profundidade 5!
rndforest = RandomForestClassifier(n_estimators = 1000 , criterion = 'gini', max_depth = 5)
#aqui passamos os requisitos para construçao das arvores !
rndforest.fit(x_train, y_train)

#aqui temos a probabilidade da coluna Target que são os nossos sobreviventes!
#dropando de dados o Target pedindo a probabilidade usando o .predict_proba() no objeto criado rndforest
probabilidade = rndforest.predict_proba(dados.drop('Target', axis=1))[:,1]
#apresentamos a classificação se é homem ou mulher!
classificacao = rndforest.predict(dados.drop('Target', axis = 1))

dados['probabilidade'] = probabilidade
dados['classificacao'] = classificacao
#comando abaixo só usado no jupyter!
dados

dados.describe()

print(dados['Sex_F'], dados['probabilidade'])
