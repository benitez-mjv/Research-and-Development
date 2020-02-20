# LIMPANDO TELA (SCREEN)
import os
os.system('cls' if os.name == 'nt' else 'clear')

# IMPORTANDO BIBLIOTECAS
print('IMPORTANDO BIBLIOTECAS NECESSÁRIAS')
import pandas as pd
import urllib.request
import lxml.html
import pyodbc
import sqlalchemy

# MAPEANDO URL VARIÁVEL DO ARQUIVO ANP
print('MAPEANDO URL ATUAL- ANP')
url = "http://www.anp.gov.br/distribuicao-e-revenda/distribuidor/combustiveis-liquidos/relacao-dos-distribuidores-bases-cessoes-de-espaco-contrato-de-fornecimento-quotas-e-entregas" 
result = urllib.request.urlopen(url)
rawContent = result.read()
html = rawContent.decode("utf8")
result.close()
doc = lxml.html.fromstring(html)
links = doc.xpath('//a/@href')

# CRIANDO VARIÁVEL VAZIA PARA RECEBER A URL MAPEADA
print('URL ATUALIZADA - ANP')
url_anp = ''
print('COMPLEMENTANDO URL - ANP')
print('')
for link in links:
  if link.startswith("/arquivos/distribuicao-revenda/distr/cl/rdbc/cessao-espaco-carregamento") and link.endswith(".xlsx"):
    print('O link atual é:'+ link)
    url_anp = "http://www.anp.gov.br"+link # Completando o link
print('')
print('CRIANDO DATA FRAME')
# CRIANDO UM DATAFRAME DIRETO DA URL MAPEADA
df = pd.read_excel(url_anp, skiprows=4)
print('')
print(df)