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

#funçoes para abrir excel e colar dados
def abrir_arquivo():
 arquivo = load_workbook('GOV BA Limite cartão.xlsx')
 planilha= arquivo.active
 return planilha

def colar_dados(planilha):
  
  dados = pyperclip.paste()
  linhas = dados.split("\n")
  for i, linha in enumerate(linhas):
     valores = linha.split("\t")
     for j, valor in enumerate(valores):
            planilha.cell(row=i+1, column=j+1).value = valor

#abrindo site
driver.get("(https://www.saopauloconsig.org.br/home?0&3+/%27)")
time.sleep(5)
