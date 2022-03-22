'''
 Algoritmo
 Passo 1 - Entender o desafio
 Passo 2 - Entender Área/Empresa
 Passo 3 - Extração/Obtenção de dados
 Passo 4 - Ajuste de dados (Tratamento/Limpeza)
 Passo 5 - Análise Exploratória
 Passo 6 - Modelagem + Algoritmos (Ciencia Artificial se necessário)
 Passo 7 - Interpretação de Resultados
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# TV[kR$] / Radio[kR$] / Jornal[kR$] / Vendas[Mi R$]
tabela = pd.read_csv('advertising.csv')


# Passo 4 (Não será necessário pois a BD já está organizada)

# Passo 5 - Análise Exploratória
# Analisar relação entre cada item

sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)

plt.show()

# Machine-Learning
# -> Separa a BD em dados de treino e dados de teste
# -> Separar tipos de dados entre x e y (x = necessários para fazer a previsão, y = dados que vão ser previstos)

y = tabela['Vendas']
x = tabela[['TV', 'Radio', 'Jornal']]

# Divide a BD em quatro novas tabelas (random_state = 1, embaralha de forma aleatória apenas 1 vez, não toda vez)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

# Vai ser utilizado dois modelos (Regressão Linear e RandomForest[Árvore de decisão])

# cria modelos
modeloRegressaoLinear = LinearRegression()
modeloArvoreDecisao = RandomForestRegressor()

#Treinar modelos
modeloRegressaoLinear.fit(x_treino, y_treino)
modeloArvoreDecisao.fit(x_treino, y_treino)

#Testar modelos
previsaoRegressaoLinear = modeloRegressaoLinear.predict(x_teste)
previsaoArvoreDecisao = modeloArvoreDecisao.predict(x_teste)

print(metrics.r2_score(y_teste, previsaoRegressaoLinear))
print(metrics.r2_score(y_teste, previsaoArvoreDecisao))

## Para este teste Árvore de decisão foi escolhida como o modelo mais próximo

# Visualização
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsão Regressão Linear'] = previsaoRegressaoLinear
tabela_auxiliar['Previsão Árvore de Decisão'] = previsaoArvoreDecisao

sns.lineplot(data=tabela_auxiliar)
plt.show()

# Fazendo previsões
# importar novas informações para fazer a previsão

novaTabela = pd.read_csv('novos.csv')

previsao = modeloArvoreDecisao.predict(novaTabela)
print(previsao)

