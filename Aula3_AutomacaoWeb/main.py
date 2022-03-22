from selenium import webdriver                      # Controla o navegador
from selenium.webdriver.common.keys import Keys     # Usa o teclado
from selenium.webdriver.common.by import By         # Localizar os itens no navegador
import pandas as pd

# Abre navegador
navegador = webdriver.Chrome()

navegador.get('https://www.google.com/')

# Pega cotação dólar
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar', Keys.ENTER) # send_keys(primeiro comando, segundo, terceiro...)

valorDolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Paga cotação euro

navegador.get('https://www.google.com/')

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro', Keys.ENTER)

valorEuro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Pega cotação ouro

navegador.get('https://www.melhorcambio.com/ouro-hoje')

valorOuro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')

valorOuro = valorOuro.replace(',', '.')

navegador.quit()

# Atualizar base de dados

tabela = pd.read_excel('Produtos.xlsx')

cotacao = ['Dólar', 'Euro', 'Ouro']
cotacaoValor = [valorDolar, valorEuro, valorOuro]
for i in range(len(cotacao)):
    tabela.loc[tabela['Moeda'] == cotacao[i], 'Cotação'] = float(cotacaoValor[i])

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

tabela.to_excel('ProdutosModificado.xlsx', index=False)
