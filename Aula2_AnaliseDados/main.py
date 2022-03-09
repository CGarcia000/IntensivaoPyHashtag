'''
 Algoritmo
 Passo 1 - Importar a base de dados para o Python
 Passo 2 - Visualizar essa base de dados
 -> Entender as informações que você tem disponível
 -> Descobrir as falhas da base de dados
 Passo 3 - Tratamento de dados
 -> Analisar se o python tá lendo as informações no formato correto
 -> Será que existe alguma coluna completamente vazia?
 -> Será que existe alguma informação em alguma linha vazia?
 Passo 4 - Análise inicial (ampla, global)
 Passo 5 - Análise detalhada (específica, localizada)
'''

import pandas as pd
import plotly.express as px

# Passo 1

tabela = pd.read_csv('telecom_users.csv')

# Passo 2

# Deleta coluna
tabela = tabela.drop('Unnamed: 0', axis=1)

# Passo 3
# -> Analisar se o python tá lendo as informações no formato correto
# coerce -> retorna os valores que não podem ser convertidos para numerico como NaN
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
print(tabela.info())

# -> Será que existe alguma coluna completamente vazia?
tabela = tabela.dropna(how='all', axis=1)

# -> Será que existe alguma informação em alguma linha vazia?
tabela = tabela.dropna(how='any', axis=0)

print(tabela.info())

# Passo 4
# -> quantos clientes cancelaram e não cancelaram (%)
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format))

# Passo 5
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()





'''
Conclusões:

- Clientes tem muita chance de cancelar nos primeiros meses

- Pessoas com familia na mesma operadora tem menos chance de cancelar

- Quanto mais serviços os clientes tem, menor a chance de cancelar

- Alta taxa de cancelamento nos serviços de fibra

- Contratos mensais tem muito mais cancelamento

- Taxa de cancelamento por boleto é muito maior
'''
