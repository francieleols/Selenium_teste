#importaçoes
import openpyxl
import time
import pandas as pd
import xlrd 
import xlwt
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
# iniciando navegador 

#funçoes para abrir excel e ter acesso as cpf's da coluna A
arquivo = load_workbook('GOV BA Limite cartão.xlsx') 
planilha = arquivo.active 

coluna= 'A'
valores_coluna = []

for cell in planilha[coluna][1:]: 
    valores_coluna.append(cell.value)

#lista de login e senha 

login = [
   "francielesilva"
]
senha= [
   "Sf070124@"
]


#abrindo site 
driver.get("(https://autenticacao.bancomaster.com.br/login)")
time.sleep(5)

Login= driver.find_element (By.XPATH,'/html/body/app-root/app-login/div/div[2]/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div[3]')
Login.send_keys(login)

Senha = driver.find_element (By.XPATH,'//*[@id="mat-input-1"]')
Senha.send_keys(senha)
time.sleep(5)

driver.get("(https://autenticacao.bancomaster.com.br/)")
time.sleep(5)

# lista cpf para cadastro em plataforma

for dado in valores_coluna:
    campo = driver.find_element(By.ID, "campo")  
    campo.send_keys(dado)

    driver.get(dir_forms)
time.sleep(1)
num_cpf = 480  # Limitador de consultas
contador = 0

for index, row in dt_total.iterrows():
    contador += 1
    if num_cpf == contador:
        print("TROCAR DE USUÁRIO")
        driver.quit()
        break