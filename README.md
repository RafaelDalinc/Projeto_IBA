# Raspagem de Dados Web

Criação de um código para extrair informações de um site web: nome e descrição das empresas listas no site.

Este projeto usou as seguintes bibliotecas: selenium.webdriver, time, openpyxl e urlib

Observação: como o site tem várias páginas, inclui um controle da última página através do tamanho de uma lista com o elemento da tela que só aparece na última página. Caso a lista seja == 0, continuo paginando e acrescentando 1 na numeração de página, caso a lista esteja == 1, pega as informações da última página e encerro o programa e salvo as informações em uma planilha excel.
