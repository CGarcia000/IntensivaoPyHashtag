'''
 Algoritmo
 Passo 1 - Entrar no sistema da empresa (no caso o drive)
 Passo 2 - Navegar no sistema até encontrar a base de dados
 Passo 3 - Exportat a base de vendas
 Passo 4 - Calcularia os indicadores (faturamento e quantidade de produtos vendidos
 Passo 5 - Enviar um email para a diretoria com os indicadores
'''

import pyautogui
import pyperclip
import time
import pandas as pd

def copiaCola(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')

# Passo 1

# Pausa entre os comandos
pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

copiaCola('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.press('enter')

#espera por 3 segundos para executar as próximas linhas
time.sleep(3)

#pyautogui.hotkey('ctrl', 't')

# Passo 2

# Posição minimizada na esquerda
    #x=1220, y=336
# Posição maximizada
    #x=407, y=264

pyautogui.click(x=407, y=264, clicks=2)
time.sleep(2)

# Passo 3
#Posições dos cliques no documento e nos dowloads
# Docs
    #x=437, y=452
pyautogui.click(x=437, y=452)
time.sleep(2)
# Tres pontos
    #x=1712, y=154
pyautogui.click(x=1712, y=154)
time.sleep(2)
# Download
    #x=1501, y=556
pyautogui.click(x=1501, y=556)

time.sleep(5)


# Passo 4

tabela = pd.read_excel(r"C:\Users\Cecilia\Downloads\Vendas - Dez.xlsx")

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
print(faturamento)
print(quantidade)

# Passo 5
pyautogui.hotkey('ctrl', 't')
copiaCola('https://mail.google.com/mail/u/0/#inbox')
pyautogui.press('enter')

time.sleep(3)

# Posição
# Escrever
    #x=71, y=173
pyautogui.click(x=71, y=173)
time.sleep(1)
pyautogui.write('cgarcia.silveira433@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
copiaCola('Intensivão Python - Teste de Automação')
pyautogui.press('tab')
email = f'''
Prezados, bom dia

O faturamento do mês foi de: R$ {faturamento:.2f}
A quantidade de produtos vendidos foi de: {quantidade}

Abs
Cecis
'''
copiaCola(email)
pyautogui.hotkey('ctrl', 'enter')
#pyautogui.press('tab')
#pyautogui.press('enter')
