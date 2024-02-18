from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from urllib.parse import quote
from selenium.webdriver.common.by import By

#instanciando o webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

#chamando o site e aguardando montagem da página
driver.get('https://www.')
driver.maximize_window()

while len(driver.find_elements('xpath', '/html/body/div[1]/div[2]/div/div/div[2]/div/div/ul/li[7]/a')) < 1:
    
    sleep(1)

#criando as listas para receber as informações
lista_resultados = []
lista_descricao = []

#criando a planilha excel
book = openpyxl.Workbook()

#criando uma plahilha e colunas.
book.create_sheet('empresas_techireland')
fintech_page = book['empresas_techireland']
fintech_page.append(['nome_empresas', 'descricao', 'setor'])

def gravar_infos(lista1, lista2):
    """
    Esta função recebe duas listas com as informações do site e 
    grava na planilha os itens das listas.
    
    list1 => lista com o nome das empresas
    list2 => lista com a descrição das empresas
    
    """
    for resultado, descricao in zip(lista_resultados, lista_descricao):
        nome = resultado.text
        desc = descricao.text   
        fintech_page.append([nome, desc])    
              

#pegar informações da primeira página
lista_resultados = driver.find_elements('xpath', '//h2[@class="text-left"]')
sleep(1)
lista_descricao = driver.find_elements('xpath', '//p[@class="text-left"]')
sleep(1)
gravar_infos(lista_resultados, lista_descricao)

pagina = 1

#pegar informações das próximas páginas
while True:
    lista_ultima_pagina = len(driver.find_elements('xpath','//li[@class="last next"]'))
    
    if lista_ultima_pagina == 1:
        pagina += 1
        driver.find_element('xpath', f'//a[@href="/companies?page={pagina}"]').click()
        driver.refresh()
        lista_resultados = driver.find_elements('xpath', '//h2[@class="text-left"]')
        sleep(1)
        lista_descricao = driver.find_elements('xpath', '//p[@class="text-left"]')
        sleep(1) 
        gravar_infos(lista_resultados, lista_descricao)
           
    elif lista_ultima_pagina == 0:
        lista_resultados = driver.find_elements('xpath', '//h2[@class="text-left"]')
        sleep(1)        
        gravar_infos(lista_resultados, lista_descricao)
        break                        
  
book.save('fintech.xlsx')
print('Informações salvas na planilha')

driver.close()


